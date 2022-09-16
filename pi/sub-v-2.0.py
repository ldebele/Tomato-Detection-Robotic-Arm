#!/usr/bin/env python3

import can
import numpy
import time
import os
import roslib
import roslib
import rospy
from std_msgs.msg import Float32MultiArray



def callback(data):
    rospy.loginfo("Message is being sent")
    val = 600*data.data
    pos_1 = val[0]
    pos_2 = val[1]
    pos_3 = val[2]
    pos_4 = val[3]
    pos_5 = val[4]
    pos_6 = val[5]

    statusMsg1 = can.Message(arbitration_id=0x141, data=[0x9C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    bus.send(statusMsg1)

    receivedMsg1 = bus.recv(10)

    if receivedMsg1 is None:
     print("did not connect")
    else:
     print("connected")
     print(receivedMsg1)


    positionMsg1 =can.Message(arbitration_id=0x140, data=[0xA4, 0x00, 0x0E, 0x01, (pos_1)&0xFF, (pos_1>>8)&0xFF,(pos_1>>16)&0xFF,(pos_1>>24)&0xFF], is_extended_id=False)
    positionMsg2 =can.Message(arbitration_id=0x141, data=[0xA4, 0x00, 0x0E, 0x01, (pos_2)&0xFF, (pos_2>>8)&0xFF,(pos_2>>16)&0xFF,(pos_2>>24)&0xFF], is_extended_id=False)
    positionMsg3 =can.Message(arbitration_id=0x142, data=[0xA4, 0x00, 0x0E, 0x01, (pos_3)&0xFF, (pos_3>>8)&0xFF,(pos_3>>16)&0xFF,(pos_3>>24)&0xFF], is_extended_id=False)
    positionMsg4 =can.Message(arbitration_id=0x143, data=[0xA4, 0x00, 0x0E, 0x01, (pos_4)&0xFF, (pos_4>>8)&0xFF,(pos_4>>16)&0xFF,(pos_4>>24)&0xFF], is_extended_id=False)
    positionMsg5 =can.Message(arbitration_id=0x144, data=[0xA4, 0x00, 0x0E, 0x01, (pos_5)&0xFF, (pos_5>>8)&0xFF,(pos_5>>16)&0xFF,(pos_5>>24)&0xFF], is_extended_id=False)
    positionMsg6 =can.Message(arbitration_id=0x145, data=[0xA4, 0x00, 0x0E, 0x01, (pos_6)&0xFF, (pos_6>>8)&0xFF,(pos_6>>16)&0xFF,(pos_6>>24)&0xFF], is_extended_id=False)

    
    try:
        bus.send(positionMsg1)
        bus.send(positionMsg2)
        bus.send(positionMsg3)
        bus.send(positionMsg4)
        bus.send(positionMsg5)
        bus.send(positionMsg6)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print('Message NOT sent.')

    
    rospy.loginfo(rospy.get_caller_id() + " I recieved data.")


def listener():
    rospy.init_node('listener')
    rospy.Subscriber("/ur/joint_position_controller/command", Float32MultiArray, callback)
    rospy.spin()


if __name__=='__main__':
    os.system('sudo ifconfig can0 down')
    os.system('sudo ip link set can0 type can bitrate 1000000')
    os.system('sudo ifconfig can0 up')
    rospy.loginfo("can is up")

    try:
        bus = can.interface.Bus(bustype='socketcan', channel='can0')
        rospy.loginfo("The bus is connected")
    except:
        print("No PICAN board found.")
        time.sleep(2)
        exit()
    

    listener()