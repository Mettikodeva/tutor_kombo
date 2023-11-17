import rospy
from std_msgs.msg import Int32


if __name__ == "__main__":
    rospy.init_node("talker")
    pub = rospy.Publisher("chatter", Int32, queue_size=10)
    rate = rospy.Rate(1)
    count = 0

    for i in range(100):
        pub.publish(i)
        if i % 5 == 0:
            pub.publish(i)
        if rospy.is_shutdown():
            break
        rate.sleep()


    # while not rospy.is_shutdown():

    #     # hello_str = "hello world %s" % rospy.get_time()
    #     # hello_str = "hello world " + str(rospy.get_time())
    #     hello_str = f"hello world {count}" 

    #     rospy.loginfo(hello_str)
    #     pub.publish(hello_str)
    #     count += 1
    #     rate.sleep()


    