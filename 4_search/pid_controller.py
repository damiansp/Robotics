# -----------
# User Instructions
#
# Implement a P controller by running 100 iterations
# of robot motion. The steering angle should be set
# by the parameter tau so that:
#
# steering = -tau_p * CTE - tau_d * diff_CTE - tau_i * int_CTE
#
# where the integrated crosstrack error (int_CTE) is
# the sum of all the previous crosstrack errors.
# This term works to cancel out steering drift.
#
# Your code should print a list that looks just like
# the list shown in the video.
#
# Only modify code at the bottom!
# ------------

from math import *
import random
from robot import *

def run(param1, param2, param3):
    myrobot = robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    N = 100
    myrobot.set_steering_drift(10. / 180. * pi) # wheels 10 deg misalignment
    old_CTE = myrobot.y
    integral = 0.

    for i in range(N):
        # Cross-track Error:
        CTE = myrobot.y
        integral += CTE
        steering = -param1 * CTE - param2 * (CTE - old_CTE) - param3 * integral
        myrobot = myrobot.move(steering = steering, distance = speed)
        old_CTE = CTE
        print myrobot
        
# Call your function with parameters of 0.2 and 3.0 and print results
run(0.2, 3.0, 0.004)
