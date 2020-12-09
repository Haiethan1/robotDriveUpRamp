#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerRequest
from nav_msgs.srv import GetMap, GetMapRequest
import time as t 


#init a node as usual
rospy.init_node('service_client')

#wait for this service to be running
rospy.wait_for_service('/box')

#create the connection to the service. Remember it's a trigger service
sos_service = rospy.ServiceProxy('/box', Trigger)

sos = TriggerRequest()

while True:

    tick = t.time()
    result = sos_service(sos) 
    tock = t.time() 


    #print (tock - tick)
    t.sleep(0.02)


print result