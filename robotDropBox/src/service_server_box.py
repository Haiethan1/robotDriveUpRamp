#! /usr/bin/env python
import rospy
from std_srvs.srv import Trigger, TriggerResponse

import os
import time as t
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
import numpy as np



name = 'box'
box_i = 0

robot_proxy = None 



def trigger_response(request):
    global box_i
    dropBoxBool = False
    a = getRobotLocation()
    x = a[0]
    y = a[1]

    b = getBoxLocation(x, y) 
    if(b != None):
        if (not checkBoxLocation(b[0], b[1])):
            dropBox(b[0], b[1])
            dropBoxBool = True
            print ("Box x val = " + str(b[0]) + " Box y val = " + str(b[1]))

    return TriggerResponse(
        success=dropBoxBool,
        message="ooo"
    )


def delBox(numBox):
    buff = "rosservice call gazebo/delete_model " + name + str(numBox)
    os.system(buff)


def delBoxAll(numBox):
    for i in range(numBox):
        delBox(i)
        t.sleep(0.1)

box_x = []
box_y = []

def saveBoxVal(x,y):
    global box_x, box_y
    box_x.append(x)
    box_y.append(y)
    return


def checkBoxLocation(x, y):
    global box_x, box_y
    for i in range(len(box_x)):
        xx = box_x[i]
        yy = box_y[i]
        d = np.sqrt((xx-x)*(xx-x) + (yy-y)*(yy-y))
        if d < 1:
            return True # return true if within 0.5m
    return False


def dropBox(x, y):
    global box_i

    saveBoxVal(x, y)

    b0 = "./load_box.sh "
    b1 = name + str(box_i) + " "
    box_i += 1

    b2 = str(y) + " "
    b3 = str(x) + " "
    b4 = "&"

    buff = b0 + b1 + b2 + b3 + b4

    os.system(buff)


def getBoxLocation(x , y):
    
    # math for circle
    # determine if it is inside of the 50m - 2m circle (for our proj, square)
    x0 = abs(x)
    y0 = abs(y)
    if (x0 > 23 or y0 > 23):
        if(x0 > 23 and y0 > 23):
            if(x > 23):
                xVal = 25
            else:
                xVal = -28
            if(y > 23):
                yVal = 25
            else:
                yVal = -28
            print("xVal = " + str(xVal) + " yVal = " + str(yVal))
            return (xVal, yVal)
        elif(x0 > 23):
            if(x > 23):
                xVal = 25
            else:
                xVal = -28
            return (xVal, y)
        else:
            if(y > 23):
                yVal = 25
            else:
                yVal = -28
            return (x, yVal)
    else:
        return None

    return



def getRobotLocation():
    global robot_proxy
    a = GetModelStateRequest(model_name = 'dd_robot')
    a.model_name = "dd_robot"
    s = robot_proxy(a)

    x = s.pose.position.x
    y = s.pose.position.y


    print "x = " + str(x) + "y = " + str(y)
    return (x, y)



rospy.init_node('service_example')
my_service = rospy.Service(
    '/box', Trigger, trigger_response
)


rospy.wait_for_service('/gazebo/get_model_state')
robot_proxy = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)


rospy.spin()