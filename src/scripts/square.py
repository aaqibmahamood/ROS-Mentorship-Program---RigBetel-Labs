#!/usr/bin/env python3
import rospy
from geometry_msgs.msg  import Twist

def rectangle():
    rospy.init_node('rectangle', anonymous=True)
    pub = rospy.Publisher("/turtlesim1/turtle1/cmd_vel", Twist, queue_size=20)
    rate = rospy.Rate(1)#hz
    vel_msg = Twist()
    rate.sleep()
    
    for i in range(4):
        #Forward
        vel_msg.linear.x = 2 # m/s
        vel_msg.angular.z = 0 # r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Stop
        vel_msg.linear.x = 0 # m/s
        vel_msg.angular.z = 0 # r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Turn
        vel_msg.linear.x = 0 # m/s
        vel_msg.angular.z= 1.57 #r/s
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    rectangle()
