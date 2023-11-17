import rospy
from tutor_kombo.srv import custom, customResponse

aktif = False

def handle(req):
    rospy.loginfo("Request received")    

    if req.tanya == "hi":
        return customResponse("hi juga")
    elif req.tanya == "halo":
        return customResponse("halo juga")
    
    elif req.tanya == "on":
        global aktif
        aktif = True
        return customResponse("service aktif")
    

if __name__ == "__main__":
    rospy.init_node("service_server")
    rospy.loginfo("Service server started")
    service = rospy.Service("tanya_jawab", custom, handle)
    while not rospy.is_shutdown():

        if aktif:
            pub = rospy.Publisher("chatter", custom, queue_size=10)
            pub.publish("service aktif")
        else:
            pub.unregister()