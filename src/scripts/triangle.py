#!/usr/bin/env python3
import rospy
from geometry_msgs.msg  import Twist

def triangle():
    rospy.init_node('triangle', anonymous=True)
    pub = rospy.Publisher("/turtlesim3/turtle1/cmd_vel", Twist, queue_size=20)
    rate = rospy.Rate(1) #hz
    vel_msg = Twist()
    rate.sleep()
    
    for i in range(3):
        #Forward
        vel_msg.linear.x = 3 #m/s
        vel_msg.angular.z = 0 #r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Stop
        vel_msg.linear.x = 0 #m/s
        vel_msg.angular.z = 0 #r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Turn
        vel_msg.linear.x = 0 #m/s
        vel_msg.angular.z = 2.0943951024 #r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Stop
        vel_msg.linear.x = 0 # m/s
        vel_msg.angular.z = 0 # r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Forward
        vel_msg.linear.x = 3 #m/s
        vel_msg.angular.z = 0 #r/s
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    triangle()
