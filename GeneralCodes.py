#Finalized code versions

#Create a uniform distribution over a matrix of arbitrary no. of rows and cols.
# M: the matrix of world states
# returns uniform distribution
def uniform(M):
    n = 0.0 #place holder for no. of cells
    q = []  #place holder for uniform distribution
    for i in range(len(M)):
        q.append([])
        for j in range(len(M[i])):
            n += 1
            q[i].append([])
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] = 1/n
    return q


#Update probability distribution based on observed measurement
# p = prior, world = map of known values for correct measurements,
# sensor_right = probablity of accurate measurement
# returns posterior distribution
def sense(p, measurement, world, sensor_right):                                     
    q = []
    for i in range(len(p)):
        q.append([])
        qSum = 0
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (measurement == world[i][j]) #hits = 1, misses = 0
            updatedValue = ( p[i][j] * (hit * sensor_right + (1 - hit) *
                             (1-sensor_right)) )
            q[i].append(updatedValue)
            qSum += updatedValue
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] /= qSum
    return q

#Update probability distribution after (attempted) movement
# p = prior, motion = [int, int] = [units_down, units_right],
# p_move = prob of accurate movement (else = no movement)
# returns posterior distribution
def move(p, motion):
    q = []
    for i in range(len(p)):
        q.append([])
    for i in range(len(p)):
        for j in range(len(p[i])):
            #successful move:
            s = p_move * (p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])])
            #failure to move:
            s += (1 - p_move) * p[i][j]
            q[i].append(s)
    return q

