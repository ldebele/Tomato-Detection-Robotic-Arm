#!/usr/bin/env python3

import rospy
import time
import numpy as np
import cv2 as cv
from std_msgs.msg import Float64
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image


UNRIPE_DIR = './src/unripe.txt'
RIPE_DIR = './src/ripe.txt'
                    

model = model_from_json(open("/home/lemi/Documents/ur_ws/src/scripts/src/model/model_arch.json", "r").read())
model.load_weights('/home/lemi/Documents/ur_ws/src/scripts/src/model/model_weights.h5')

class Talker:
    def __init__(self):
        self.pub1 = None 
        self.pub2 = None 
        self.pub3 = None 
        self.rate = None


    def talker(self):
        self.pub1 = rospy.Publisher('/ur/joint1_positon_controller/command', Float64, queue_size=10)
        self.pub2 = rospy.Publisher('/ur/joint2_position_controller/command', Float64, queue_size=10)
        self.pub3 = rospy.Publisher('/ur/joint3_position_controller/command', Float64, queue_size=10)

        
        rospy.init_node('talker', anonymous=True)
        self.rate = rospy.Rate(10)

        cap = cv.VideoCapture(0)
        backgroundobject = cv.createBackgroundSubtractorMOG2()


        while not rospy.is_shutdown():
            ret, frame = cap.read()
            fgmask = backgroundobject.apply(frame)
            _, thresh = cv.threshold(fgmask, 250, 255, cv.THRESH_BINARY)

            #img_erode = cv.erode(thresh, None, iterations=1)
            #img_dilate = cv.dilate(img_erode, None, iterations=2)

            contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            ret, frame = cap.read()

            if len(contours) > 20:
                c = max(contours, key=cv.contourArea)
                x,y,w,h = cv.boundingRect(c)
                cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
                croped_img = frame[y:y+h, x:x+w]

                cv.imshow('Stream', frame)
                if cv.waitKey(1) and 0xFF == ord('q'):
                    break

                # resize the image
                resized_img = cv.resize(croped_img, (300, 300), interpolation = cv.INTER_AREA)
                image_pixels = image.img_to_array(resized_img)
                image_pixels = np.expand_dims(image_pixels, axis=0)
                image_pixels /= 255.
                predictions = model.predict(image_pixels)
                max_index = np.argmax(predictions[0])
                tomato_detection_dict = ('background', 'Red', 'Green')
                tomato_prediction = tomato_detection_dict[max_index]
                # print(tomato_prediction)

                if tomato_prediction == 'Green':
                   self.pub_trajectory(UNRIPE_DIR, 'Green')
                elif tomato_prediction == 'Red':
                    self.pub_trajectory(RIPE_DIR, 'Red')
                 
                time.sleep(2)

    def pub_trajectory(self, path, tomato_type):
        print(tomato_type)
        trajectory = np.genfromtxt(path)
        for i in range(trajectory.shape[1]):
            j1 = trajectory[0, i]
            j2 = trajectory[1, i]
            j3 = trajectory[2, i]

            print(f'Values for the first motor {j1}')
            print(f'Values for the second motor {j2}')
            print(f'Values for the thrid motors {j3}')
            rospy.loginfo('Data is being sent for red trajectory')
            self.pub1.publish(j1)
            self.pub2.publish(j2)
            self.pub3.publish(j3)
            time.sleep(0.5)
            self.rate.sleep()



if __name__=='__main__':

    Talker.talker()

