#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from nav_msgs.msg import OccupancyGrid
import numpy as np

state = 0
OriginX =0
OriginY = 0
w= 0
h =0
reso = 0
map1D = []



def getData(data):
	#print(type(data))
	#global OriginX,OriginY,w,h,reso

	x = data.info.point.position.x # C'est la postion orginal 
	y = data.info.point.position.y # de la map en -10;-10
	print(x,y)


   
    
def listener():
	global state
	rospy.init_node('listener', anonymous=True)
	
	rospy.Subscriber("pose", Pose,getData)
	# spin() simply keeps python from exiting until this node is stopped
	
	rospy.spin()

if __name__ == '__main__':
	listener()
