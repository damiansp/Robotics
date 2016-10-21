# -----------
# User Instructions
#
# Implement a P controller by running 100 iterations
# of robot motion. The desired trajectory for the
# robot is the x-axis. The steering angle should be set
# by the parameter tau so that:
#
# steering = -tau * crosstrack_error
#
# Note that tau is called "param" in the function
# below.
#
# Your code should print output that looks like
# the output shown in the video. That is, at each step:
# print myrobot, steering
#
# Only modify code at the bottom!
# ------------

from math import *
import random
from robot import *

def run(param):
    myrobot = robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    N = 100

    # Cross-track error:
    for i in range(N):
        cte = myrobot.y
        myrobot = myrobot.move(steering = -param * cte, distance = speed)
        print myrobot
        

run(0.1) # call function with parameter tau of 0.1 and print results
                                                                
