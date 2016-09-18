#!/usr/bin/env python
colors = [['red', 'green', 'green', 'red' ,  'red'],
          ['red', 'red',   'green', 'red',   'red'],
          ['red', 'red',   'green', 'green', 'red'],
          ['red', 'red',   'red',   'red',   'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 0.7
p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

def sense(p, Z):    #p = prior, Z = measurement, observation
    q = []

    for i in range(len(p)):
        q.append([])
        qSum = 0

    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (Z == colors[i][j]) #hits = 1, misses = 0
            updatedValue = (p[i][j] * (hit * sensor_right + (1 - hit) * (1-sensor_right)))
            q[i].append(updatedValue)
            qSum += updatedValue

    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] /= qSum

    return q



def move(p, U):
    q = []

    for i in range(len(p)):
        q.append([])

    for i in range(len(p)):
        for j in range(len(p[i])):
            #successful move:
            s = p_move * (p[(i - U[0]) % len(p)][(j - U[1]) % len(p[i])])
            #failure to move:
            s += (1 - p_move) * p[i][j]
            q[i].append(s)

    return q



def uniform(world):
    n = 0.0 #no. of cells
    q = []

    for i in range(len(world)):
        q.append([])
        for j in range(len(world[i])):
            n += 1
            q[i].append([])

    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] = 1/n

    return q


p = uniform(colors)

for k in range(len(motions)):
   p = move(p, motions[k])
   p = sense(p, measurements[k])
    


#Your probability array must be printed 
#with the following code.

show(p)




