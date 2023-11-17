
import rospy
from std_msgs.msg import String


def main():
	rospy.init_node("pembicara")
	rospy.loginfo("Pembicara dimulai")
	pub = rospy.Publisher("topik", String, queue_size=10)
	rate = rospy.Rate(1)
	count = 0
	while not rospy.is_shutdown():
		# msg = "Hallo Dunia! " + str(count)
		# msg = "Hallo Dunia! %s" %count
		# msg = "Hallo Dunia! {}".format(count)
		msg = f"Hallo Dunia! {count}"
		rospy.loginfo(msg)
		pub.publish(msg)
		count = count + 1
	
	
		
	
	






