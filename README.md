# imu_visualization
IMU Sensor Visualization with ROS and Arduino Mega

This repository contains code to visualize IMU sensor data from an Arduino Mega connected to the BNO055 IMU sensor using ROS Noetic.

Prerequisites

- ROS Noetic installed [Installation Guide](http://wiki.ros.org/noetic/Installation)
* Arduino Mega connected to the BNO055 IMU sensor
+ rosserial_python package installed [Installation Guide](http://wiki.ros.org/rosserial_python)
- RViz installed [Installation Guide](http://wiki.ros.org/rviz/UserGuide#Install_or_build_rviz)

Setup

    1.Connect your Arduino Mega to the BNO055 IMU sensor.
    2.Clone this repository into your ROS workspace:

bash

    https://github.com/RobosocNITH-ROS/IMU_visualization.git

Open a terminal and run the rosserial serial node to establish communication between Arduino and ROS:

bash

rosrun rosserial_python serial_node.py /dev/ttyUSB0 
(Note: It may happen that your Arduino_ide shows another port apart from USB0(eg: ACM0), you may replace "USB0" as required.)

Open another terminal and launch RViz with the pre-configured display for IMU visualization:

bash

    rviz -d imu_display.rviz

## Video Demonstration

Check out this video demonstrating the IMU sensor visualization:

[Direct link to video](https://youtu.be/5yBu7VM4hyY)


Notes

    1.Make sure your Arduino is properly configured to send IMU sensor data.
    2.The imu_display.rviz file contains the RViz configuration for visualizing the IMU sensor data. Adjust it according to your requirements.
    3.Modify the topic names in imu_display.rviz if your ROS topics differ from the defaults.

Contact

For any issues or suggestions, please contact:

    Aakash Tiwari - aakashtiwari07.12.2003@gmail.com
    Robotics Society, NIT Hamirpur - robonith@nith.ac.in
