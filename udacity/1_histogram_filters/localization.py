#!/usr/bin/env python

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']

# Sensor value
measurements = ['red', 'red']
# Intended motions
motions = [1, 1]

# Multiplier for accurate (pHit) and inaccurate (pMiss) sensor readings
pHit = 0.6
pMiss = 0.2

# Probability of successful move
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# Modify the code below so that the function sense, which takes p and Z as inputs, will output
# the normalized probability distribution, q, after multiplying the entries in p by pHit or
# pMiss according to the color in the corresponding cell in world.

def sense(p, Z):
    q = []

    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit*pHit + (1 - hit)*pMiss))

    normalizer = sum(q)
    
    for i in range(len(q)):
        q[i] /= normalizer

    return(q)


def move(p, U):
    '''Probability distribution after intending to move right U units'''
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s += pOvershoot * p[(i - U - 1) % len(p)]
        s += pUndershoot * p[(i - U + 1) % len(p)]
        q.append(s)

    return (q)

for c in range(len(measurements)):
    p = sense(p, measurements[c])
    p = move(p, motions[c])

print (p)
