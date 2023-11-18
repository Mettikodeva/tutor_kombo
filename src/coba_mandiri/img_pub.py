import rospy
import cv2 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np


def send_image(img, pub):
    bridge = CvBridge()
    msg_frame = bridge.cv2_to_imgmsg(img, 'bgr8')
    # publish pesan dibawah
    ...

def on_shutdown():
    rospy.loginfo("Shutdown")
    # cap.release()

if __name__ == "__main__":
    # cap = cv2.VideoCapture(0)
    frame = np.empty((480, 640, 3), dtype=np.uint8)
    cv2.PutText(frame, "Hello World", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                   
    
    # write the needed ROS Code here:
    # 1. Initialize the node
    # 2. Initialize the publisher named pub
    ...
    rospy.on_shutdown(on_shutdown)
    r = rospy.Rate(30)
    pub =  ...


    while not rospy.is_shutdown():
        # ret, frame = cap.read()
        send_image(frame, pub)
        r.sleep()
    
       