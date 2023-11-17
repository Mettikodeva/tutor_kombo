import rospy
from tutor.srv import TanyaJawab, TanyaJawabResponse

def handle_tanya_jawab(req):

    rospy.loginfo(f"Request: {req.tanya}")
    if req.tanya.lower() == "siapa namamu":
        return TanyaJawabResponse("Namaku ROS")
    elif req.tanya.lower() == "hi":
        return TanyaJawabResponse("Hallo")
    elif req.tanya.lower() == "hallo":
        return TanyaJawabResponse("Hi")
    else:
        return TanyaJawabResponse("Maaf, aku tidak mengerti")



if __name__ == "__main__":
    rospy.init_node("service_server")
    service_server = rospy.Service("tanya_jawab", TanyaJawab, handle_tanya_jawab)
    rospy.loginfo("Service server is ready")
    rospy.spin()
