import rospy
from tutor.srv import TanyaJawab, TanyaJawabResponse

if __name__ == "__main__":
    rospy.init_node("service_client")
    rospy.wait_for_service("tanya_jawab")
    try:
        service_client = rospy.ServiceProxy("tanya_jawab", TanyaJawab)
        tanya = input("Tanya: ")
        response = service_client(tanya)
        rospy.loginfo(f"Jawaban {response}")
    except rospy.ServiceException as e:
        rospy.logwarn(f"Service call failed: {e}")
    print("Done")