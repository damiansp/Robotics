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
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.show()

    # Error tracking
    print ("Error:", eval(myrobot, p))
    
print p[:5]  # note orientations also converging



# Circular movement---------------------------------------------------
# position of 4 landmarks
landmarks  = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]]
# world is NOT cyclic. Robot is allowed to travel "out of bounds"
world_size = 500.0
max_steering_angle = pi/4

# Test case 1:
length = 20.
bearing_noise  = 0.0
steering_noise = 0.0
distance_noise = 0.0

myrobot = robot(length)
myrobot.set(0.0, 0.0, 0.0)
myrobot.set_noise(bearing_noise, steering_noise, distance_noise)

motions = [[0.0, 10.0], [pi / 6.0, 10], [0.0, 20.0]]
T = len(motions)

print 'Robot:    ', myrobot
for t in range(T):
    myrobot = myrobot.move_circular(motions[t])
    print 'Robot:    ', myrobot

# Test Case 2:
myrobot.set(0.0, 0.0, 0.0)
motions = [[0.2, 10.] for row in range(15)]
T = len(motions)

# Track motion to plot
xs = [myrobot.x]
ys = [myrobot.y]



print 'Robot:    ', myrobot
for t in range(T):
    myrobot = myrobot.move_circular(motions[t])
    xs.append(myrobot.x)
    ys.append(myrobot.y)
    print 'Robot:    ', myrobot

plt.plot(xs, ys, 'bo-')
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.show()
