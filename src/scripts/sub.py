#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String

def msgCallback(greeting):
    rospy.loginfo( "Subscriber -" + greeting.data)

def subscriber():
    rospy.init_node('sub')
    rospy.Subscriber('helloTopic', String, msgCallback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()