# ----------------
# User Instructions
#
# Implement twiddle as shown in the previous two videos.
# Your accumulated error should be very small!
#
# Your twiddle function should RETURN the accumulated
# error. Try adjusting the parameters p and dp to make
# this error as small as possible.
#
# Try to get your error below 1.0e-10 with as few iterations
# as possible (too many iterations will cause a timeout).
# No cheating!
# ------------


from math import *
import random
from robot import *

def run(params, printflag = False):
    myrobot = robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    err = 0.0
    N = 100
    myrobot.set_steering_drift(10. / 180. * pi) # wheels 10 deg misalignment

    crosstrack_error = myrobot.y

    for i in range(N * 2):
        diff_crosstrack_error = myrobot.y - crosstrack_error
        crosstrack_error = myrobot.y
        int_crosstrack_error = crosstrack_error
        
        steer = (-params[0] * crosstrack_error
                 - params[1] * diff_crosstrack_error
                 - params[2] * int_crosstrack_error)
        myrobot = myrobot.move(steering = steer, distance = speed)

        if i >= N:
            err += (crosstrack_error ** 2)

        if printflag:
            print myrobot, steer

    return err / float(N)
        

def twiddle(tol = 0.2):
    # Optimize parameters
    p  = [0, 0, 0] # params
    dp = [1, 1, 1] # new potential params to test

    best_err = run(p, True)

    while sum(dp) > tol:
        print 'params:', p
        for i in range(len(p)):
            p[i] += dp[i]
            err = run(p)

            if err < best_err:
                best_err = err
                dp[i] *= 1.1
            else:
                p[i] -= 2 * dp[i]
                err = run(p)

                if err < best_err:
                    best_err = err
                    dp[i] *= 1.1
                else:
                    p[i] += dp[i]
                    dp[i] *= 0.9

    return run(p, True)

print twiddle()
