import rospy
from geometry_msgs.msg import Twist
from gazebo_msgs.srv import GetModelState




rospy.init_node('SpawnBox', anonymous=True)


def handle_setBox(req):
    #TODO: Spawn box
    print(req)



s = rospy.Service('/box', Twist, handle_setBox)



rospy.spin()