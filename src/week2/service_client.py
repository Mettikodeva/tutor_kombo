import rospy
from tutor_kombo.srv import custom

if __name__ == "__main__":
    rospy.init_node("service_client")
    service = rospy.ServiceProxy("tanya_jawab", custom)
    data = input("tanya: ")
    result = service(data)
    rospy.loginfo(f"jawaban server: {result.jawab}")