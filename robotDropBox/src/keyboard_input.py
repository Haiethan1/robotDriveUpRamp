#! /usr/bin/env python
import rospy

from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties


speed = 200
turn = 500

def setRot(pub, msg): 
    global speed
    d = msg 
    buff = ApplyJointEffort()

    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)

    if (d == "s"):
        #pub("dd_robot::left_front_wheel_hinge", 1 * speed, start_time, end_time)
        #pub("dd_robot::right_front_wheel_hinge",  1 * speed, start_time, end_time)

        pub("dd_robot::left_back_wheel_hinge", -1 * speed, start_time, end_time)
        pub("dd_robot::right_back_wheel_hinge", -1 * speed, start_time, end_time)
    elif (d == "w"):
        #pub("dd_robot::left_front_wheel_hinge", -1 * speed, start_time, end_time)
        #pub("dd_robot::right_front_wheel_hinge", -1 * speed, start_time, end_time)
        
        pub("dd_robot::left_back_wheel_hinge", 1 * speed, start_time, end_time)
        pub("dd_robot::right_back_wheel_hinge", 1 * speed, start_time, end_time)
    elif ( d == "d"):
        pub("dd_robot::left_front_wheel_hinge", 1 * turn, start_time, end_time)
        pub("dd_robot::right_front_wheel_hinge", -1 * turn, start_time, end_time)

        #pub("dd_robot::left_back_wheel_hinge", 1 * turn, start_time, end_time)
        #pub("dd_robot::right_back_wheel_hinge", -1 * turn, start_time, end_time)

    elif (d == "a"):
        pub("dd_robot::left_front_wheel_hinge", -1 * turn, start_time, end_time)
        pub("dd_robot::right_front_wheel_hinge", 1 * turn, start_time, end_time)

        #pub("dd_robot::left_back_wheel_hinge", -1 * turn, start_time, end_time)
        #pub("dd_robot::right_back_wheel_hinge", 1 * turn, start_time, end_time)


    else:
        pass

rospy.init_node('keyboard', anonymous=True)
pub = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)


while(True):
    val = raw_input("Direction = ") #(if you want to speed up or down, type increase / decrease): 
    setRot(pub, val)



