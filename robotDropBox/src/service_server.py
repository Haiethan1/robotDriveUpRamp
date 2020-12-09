#! /usr/bin/env python
import rospy
from std_srvs.srv import Trigger, TriggerResponse

def trigger_response(request):
    return TriggerResponse(
        sucess=True,
        message="Robots, cats, but not dogs."
    )

rospy.init_node('service_example')
my_service = rospy.Service(
    '/service_example)topic', Trigger, trigger_response
)

rospy.spin()