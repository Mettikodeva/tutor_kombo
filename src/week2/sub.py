import rospy
from std_msgs.msg import Int32

def callback(data):
    print(data)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    

if __name__ == "__main__":

    rospy.init_node("listener")
    rospy.Subscriber("chatter", Int32, callback) 

    rospy.spin()