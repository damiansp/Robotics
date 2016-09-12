# Unit 1

# Create a vector of lenth n with uniform probability distribution
def uniform(n):
    p = []
    i = n
    while i > 0:
        p.append(1.0/n)
        i -= 1
    return p
    

# Update a uniform distribution p by an updating score, where hits are indices
# of values matching an observation, pHit is the multiplier for hits and
# pMiss if not a hit
p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2
hits = [1,2]

for i in range(len(p)):
    if i in hits:
        p[i] = p[i] * pHit
    else:
        p[i] = p[i] * pMiss

print(p)
print(sum(p))


# Generalize previous
world = ['green', 'red', 'red', 'green', 'green'] #state space characteristics
measurements = ['red' , 'green']  #observed value

def sense(p, Z):    #p = prior, Z = measurement, observation
    q = []
    for i in range(len(p)):
        hit = (Z == world[i]) #hits = 1, misses = 0
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    normalizer = sum(q)
    for i in range(len(q)):
        q[i] /= normalizer
    return q

for k in range(len(measurements)):
    p = sense(p, measurements[k])

print(p)


# Exact movement: update prob distribution p after a move of U units
def move(p, U):
    q = []
    
    for i in range(len(p)):
       q.append(p[(i - U) % len(p)])
    return q


#Update move for imprecise movement
p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

#My code:
def move(p, U):
    q = []
    for i in range(len(p)):
        q.append( (pExact * p[(i - U) % len(p)]) +
                  (pOvershoot * p[(i - U - 1) % len(p)]) +
                  (pUndershoot * p[(i - U + 1) % len(p)]) )
    return q

#Udacity code:
def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s += pOvershoot * p[(i-U-1) % len(p)]
        s += pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q



#HW 1.4 Localization Program
#Given:
colors = [['red', 'green', 'green', 'red',   'red'],
          ['red', 'red',   'green', 'red',   'red'],
          ['red', 'red',   'green', 'green', 'red'],
          ['red', 'red',   'red',   'red',   'red']] # = world

measurements = ['green', 'green', 'green', 'green', 'green']

motions = [[0,0], [0,1], [1,0], [1,0], [0,1]] #[1,1] = [right, down]

sensor_right = 0.7  #prob. of sensor measurement being correct

p_move = 0.8 #prob. of moving according to motions; else no move

#Write: 
p = [[0.05, 0.05, 0.05, 0.05, 0.05],
     [0.05, 0.05, 0.05, 0.05, 0.05],
     [0.05, 0.05, 0.05, 0.05, 0.05],
     [0.05, 0.05, 0.05, 0.05, 0.05]]


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
    print q
