#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu

def imu_callback(msg):
    rospy.loginfo("Received IMU data: %s", msg)

def imu_listener():
    rospy.init_node('imu_listener', anonymous=True)
    rospy.Subscriber("/imu_data", Imu, imu_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        imu_listener()
    except rospy.ROSInterruptException:
        pass

