#include "ros/ros.h"
#include "tutor/TanyaJawab.h"
#include <boost/algorithm/string.hpp>

bool jawab(tutor::TanyaJawab::Request  &req,
         tutor::TanyaJawab::Response &res)
{
    std::string s = boost::algorithm::to_lower_copy(req.tanya);
    if (s.compare("hallo") == 0)
    {
        res.jawab = "Hi";
    }
    else if (s.compare("hi") == 0)
    {
        res.jawab = "Hallo";
    }
    else
    {
        res.jawab = "Maaf, aku tidak mengerti";
    }
  ROS_INFO("request: %s", req.tanya.c_str());
  ROS_INFO("sending back response: [%s]", res.jawab.c_str());
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "tanya_jawab_server");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("tanya_jawab", jawab);
  ROS_INFO("Siap tanya jawab!.");
  ros::spin();
  return 0;
}