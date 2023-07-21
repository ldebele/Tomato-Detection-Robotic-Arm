#!/usr/bin/env python3

import can
import numpy
import time
import os
import roslib
import roslib
import rospy
from std_msgs.msg import Float64




def callback1(data):
    rospy.loginfo("Message is being sent")
    pos_1 = 600*data.data
    
    positionMsg1 =can.Message(arbitration_id=0x140, data=[0xA4, 0x00, 0x0E, 0x01, (pos_1)&0xFF, (pos_1>>8)&0xFF,(pos_1>>16)&0xFF,(pos_1>>24)&0xFF], is_extended_id=False)

    try:
        bus.send(positionMsg1)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print('Message NOT sent.')


def callback2(data):
    rospy.loginfo("Message is being sent")
    pos_2 = 600*data.data
    
    positionMsg2 =can.Message(arbitration_id=0x141, data=[0xA4, 0x00, 0x0E, 0x01, (pos_2)&0xFF, (pos_2>>8)&0xFF,(pos_2>>16)&0xFF,(pos_2>>24)&0xFF], is_extended_id=False)
    
    try:
        bus.send(positionMsg2)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print('Message NOT sent.')

def callback3(data):
    rospy.loginfo("Message is being sent")
    pos_3 = 600*data.data
    
    positionMsg3 =can.Message(arbitration_id=0x142, data=[0xA4, 0x00, 0x0E, 0x01, (pos_3)&0xFF, (pos_3>>8)&0xFF,(pos_3>>16)&0xFF,(pos_3>>24)&0xFF], is_extended_id=False)
    
    try:
        bus.send(positionMsg3)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print('Message NOT sent.')
        

# def callback4(data):
#     rospy.loginfo("Message is being sent")
#     pos_4 = 600*data.data
    
#     positionMsg4 =can.Message(arbitration_id=0x143, data=[0xA4, 0x00, 0x0E, 0x01, (pos_4)&0xFF, (pos_4>>8)&0xFF,(pos_4>>16)&0xFF,(pos_4>>24)&0xFF], is_extended_id=False)
    
#     try:
#         bus.send(positionMsg4)
#         print(f"Message sent on {bus.channel_info}")
#     except can.CanError:
#         print('Message NOT sent.')

# def callback5(data):
#     rospy.loginfo("Message is being sent")
#     pos_5 = 600*data.data
    
#     positionMsg5 =can.Message(arbitration_id=0x144, data=[0xA4, 0x00, 0x0E, 0x01, (pos_5)&0xFF, (pos_5>>8)&0xFF,(pos_5>>16)&0xFF,(pos_5>>24)&0xFF], is_extended_id=False)
    
#     try:
#         bus.send(positionMsg5)
#         print(f"Message sent on {bus.channel_info}")
#     except can.CanError:
#         print('Message NOT sent.')


# def callback6(data):
#     rospy.loginfo("Message is being sent")
#     pos_6 = 600*data.data
    
#     positionMsg6 =can.Message(arbitration_id=0x146, data=[0xA4, 0x00, 0x0E, 0x01, (pos_6)&0xFF, (pos_6>>8)&0xFF,(pos_6>>16)&0xFF,(pos_6>>24)&0xFF], is_extended_id=False)
    
#     try:
#         bus.send(positionMsg6)
#         print(f"Message sent on {bus.channel_info}")
#     except can.CanError:
#         print('Message NOT sent.')


rospy.loginfo(rospy.get_caller_id() + " I recieved data.")


def listener():
    rospy.init_node('listener')
    rospy.Subscriber("/ur/joint1_position_controller/command", Float64, callback1)
    rospy.Subscriber("/ur/joint2_position_controller/command", Float64, callback2)
    rospy.Subscriber("/ur/joint3_position_controller/command", Float64, callback3)
    # rospy.Subscriber("/ur/joint4_position_controller/command", Float64, callback4)
    # rospy.Subscriber("/ur/joint5_position_controller/command", Float64, callback5)
    # rospy.Subscriber("/ur/joint6_position_controller/command", Float64, callback6)
    rospy.spin()


if __name__=='__main__':
    os.system('sudo ifconfig can0 down')
    os.system('sudo ip link set can0 type can bitrate 1000000')
    os.system('sudo ifconfig can0 up')
    print("Can is up")

    try:
        bus = can.interface.Bus(bustype='socketcan', channel='can0')
        print("The bus is connected")
    except:
        print("No PICAN board found.")
        time.sleep(2)
        exit()
    

    listener()

