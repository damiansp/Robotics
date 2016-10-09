from robot import *
from math import *
import matplotlib.pyplot as plt
import numpy as np


myrobot = robot()

# Start robot at (30, 50, pi/2), where pi/2 indicates a North heading
myrobot.set(30, 50, pi / 2)
print (myrobot.__repr__())

# Turn right 90 deg, move 15m, sense
myrobot = myrobot.move(-pi / 2, 15)
print (myrobot.sense())
print (myrobot.__repr__())

# Turn right 90 deg, move 10m, sense
myrobot = myrobot.move(-pi / 2, 10)
print (myrobot.sense())
print (myrobot.__repr__())


# As above but with noise added
myrobot = robot()

# Set noise (forward, turn, signal)
myrobot.set_noise(5.0, 0.1, 5.0)

# Start robot at (30, 50, pi/2), where pi/2 indicates a North heading
myrobot.set(30, 50, pi / 2)

# Turn right 90 deg, move 15m, sense
myrobot = myrobot.move(-pi / 2, 15)
print (myrobot.sense())

# Turn right 90 deg, move 10m, sense
myrobot = myrobot.move(-pi / 2, 10)
print (myrobot.sense())



# Use a particle filter-----------------------------------------------
# Initialize 1000 particles
N = 5000
T = 10 # Time steps

# Intialize the robot
myrobot = robot()

# Initialize particles
p = []
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p.append(x)

for t in range(10):
    myrobot = myrobot.move(0.1, 5.0)
    Z = myrobot.sense()

    # Simulate robot's motion for all particles-- 
    for particle in range(N):
        p[particle] = p[particle].move(0.1, 5)

    
    # Set weights to each particle
    w = []
    for particle in range(N):
        w.append(p[particle].measurement_prob(Z))

    # Resample weights according to probability
    # Using my own code::
    #p_new = []
    #index = int(random.uniform(0, N))
    #beta = 0

    #for i in range(N):
    #    beta += random.uniform(0, 2 * max(w))

    #    while w[index] < beta:
    #        beta -= w[index]
    #        index = (index + 1) % N

    #    p_new.append(p[index])

    #p = p_new

    # Using numpy:
    w = np.array(w)
    p = np.random.choice(p, N, replace = True, p = w / sum(w))

    print ('Robot:', myrobot.__repr__())
    # Verify visually
    x = [a.x for a in p]
    y = [a.y for a in p]

    plt.plot(x, y, 'bo', alpha = 0.02)
    plt.show()


print p[:5]  # note orientations also converging
