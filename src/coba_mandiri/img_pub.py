import rospy
import cv2 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np


def send_image(img, pub):
    msg_frame = CvBridge().cv2_to_imgmsg(img, encoding="passthrough")
    # publish pesan dibawah
    ...

def on_shutdown():
    rospy.loginfo("Shutdown")
    cap.release()

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    
    # write the needed ROS Code here:
    # 1. Initialize the node
    # 2. Initialize the publisher named pub
    ...
    rospy.on_shutdown(on_shutdown)
    r = rospy.Rate(30)
    pub =  ...


    while not rospy.is_shutdown():
        ret, frame = cap.read()
        send_image(frame, pub)
        r.sleep()
    
       