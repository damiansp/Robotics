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
    n_params = 3
    params  = [0. for row in range(n_params)] # params
    dparams = [1. for row in range(n_params)] # new potential params to test

    best_err = run(params)
    n = 0

    while sum(dparams) > tol:
        for i in range(len(params)):
            params[i] += dparams[i]
            err = run(params)

            if err < best_err:
                best_err = err
                dparams[i] *= 1.1
            else:
                params[i] -= 2. * dparams[i]
                err = run(params)

                if err < best_err:
                    best_err = err
                    dparams[i] *= 1.1
                else:
                    params[i] += dparams[i]
                    dparams[i] *= 0.9
        n += 1
        print 'Twiddle #', n, params ' -> ', best_err
        
    return params

print twiddle()
