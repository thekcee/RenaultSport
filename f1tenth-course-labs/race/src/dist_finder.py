#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from race.msg import pid_input

# Some useful variable declarations.
angle_range = 240	# sensor angle range of the lidar
car_length = 1.5	# distance (in m) that we project the car forward for correcting the error. You may want to play with this.
desired_trajectory = 0.75	# distance from the wall (left or right - we cad define..but this is defined for right). You should try different values
vel = 15 		# this vel variable is not really used here.
error = 0.0

pub = rospy.Publisher('error', pid_input, queue_size=10)

##	Input: 	data: Lidar scan data
##			theta: The angle at which the distance is requried
##	OUTPUT: distance of scan at angle theta

def getRange(data,theta):
# Find the index of the arary that corresponds to angle theta.
# Return the lidar scan value at that index
# Do some error checking for NaN and ubsurd values
## Your code goes here
   	index = theta*(len(data.ranges)/240)
   	dist = data.ranges[int(index)]
    	if dist < data.range_min:
        	dist = data.range_min
	elif math.isnan(dist) or dist > data.range_max:
		dist = data.range_max
	return dist

def callback(data):
	theta = 100
	a = getRange(data,theta)
	b = getRange(data, 35)	# Note that the 0 implies a horizontal ray..the actual angle for the LIDAR may be 30 degrees and not 0.
	swing = math.radians(theta)

	## Your code goes here to compute alpha, AB, and CD..and finally the error.
    	alpha = math.atan((a*math.cos(swing)-b)/(a*math.sin(swing)))
   	AB = b*math.cos(alpha)

	AC = 1.5
	AD = getRange(data, theta)
    #assuming AC is distance from car to another wall at angle alpha
    	#CD = AB +  (AC * math.sin(alpha))
    	CD = AD * math.cos(math.radians(65))
    	error = desired_trajectory-CD
	rospy.loginfo('ab:' + str(AB) + ' cd:' + str(CD))

	## END

	msg = pid_input()
	msg.pid_error = error		# this is the error that you wantt o send to the PID for steering correction.
	msg.pid_vel = vel		# velocity error is only provided as an extra credit field.
	pub.publish(msg)


if __name__ == '__main__':
	print("Laser node started")
	rospy.init_node('dist_finder',anonymous = True)
	rospy.Subscriber("scan",LaserScan,callback)
	rospy.spin()
