import rospy
import cv2 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np


def img_callback(data):
    # write the needed ROS Code here:
    # 1. Convert the image message to cv2 image 
    img = ...
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    

def on_shutdown():
    rospy.loginfo("Shutdown")
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    
    # write the needed ROS Code here:
    # 1. Initialize the node
    # 2. Initialize the subscriber
    ...
    rospy.on_shutdown(on_shutdown)
    ...

    rospy.spin()