
import rospy
from std_msgs.msg import String


def callback(msg):
    rospy.loginfo("Pendengar menerima: %s", msg.data)

def main():
	rospy.init_node("Pendengar")
	rospy.loginfo("Pendengar dimulai")
	sub = rospy.Subscriber("topik", String, callback)
	rospy.spin()
	
	
		
	
	






