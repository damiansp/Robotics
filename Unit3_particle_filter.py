from robot import *
from math import *

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
N = 1000
p = []


# Intialize the robot move it and sense
myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense()

# Initialize particles
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p.append(x)


# Simulate robot's motion for all particles-- 
for particle in range(N):
    p[particle] = p[particle].move(0.1, 5)

    
# Set weights to each particle
w = []
for particle in range(N):
    w.append(p[particle].measurement_prob(Z))
