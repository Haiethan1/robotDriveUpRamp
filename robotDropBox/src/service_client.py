#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerRequest

#init a node as usual
rospy.init_node('service_client')

#wait for this service to be running
rospy.wait_for_service('/service_example_topic')

#create the connection to the service. Remember it's a trigger service
sos_service = rospy.ServiceProxy('/service_example_topic')

sos = TriggerRequest()

result = sos_service(sos) 

print result