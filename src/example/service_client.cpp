#include "ros/ros.h"
#include "tutor/TanyaJawab.h"


int main(int argc, char **argv)
{
  ros::init(argc, argv, "tanya_jawab_client");
  if (argc != 2)
  {
    ROS_INFO("usage: tanya aja!");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<tutor::TanyaJawab>("tanya_jawab");
  tutor::TanyaJawab srv;
  srv.request.tanya = argv[1];
  if (client.call(srv))
  {
    ROS_INFO("Jawaban: %s", srv.response.jawab.c_str());
  }
  else
  {
    ROS_ERROR("Failed to call service tanya_jawab");
    return 1;
  }

  return 0;
}