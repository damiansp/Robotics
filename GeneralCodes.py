#Finalized code versions

# Unit 1: Discrete space model
def uniform(M):
    '''
    Create a uniform distribution over a matrix of arbitrary no. of rows and 
    cols.
    @param M: the matrix of world states
    @return array of dims(M) with uniform distribution
    '''
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


def sense(p, measurement, world, sensor_right):
    '''
    Update probability distribution based on observed measurement
    @param p = prior
    @param world = map of known values for correct measurements
    @param sensor_right = probablity of accurate measurement
    @return posterior distribution
    '''
    q = []
    
    for i in range(len(p)):
        q.append([])
        qSum = 0
        
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (measurement == world[i][j]) # hits = 1, misses = 0
            updatedValue = (p[i][j] * (hit * sensor_right + (1 - hit) *
                                       (1 - sensor_right)))
            q[i].append(updatedValue)
            qSum += updatedValue
            
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] /= qSum
            
    return q


def move(p, motion):
    '''
    Update probability distribution after (attempted) movement
    @param p = prior
    @param motion = [int, int] = [units_down, units_right],
    @param p_move = prob of accurate movement (else = no movement)
    @return posterior distribution
    '''
    q = []
    
    for i in range(len(p)):
        q.append([])
        
    for i in range(len(p)):
        for j in range(len(p[i])):
            #successful move:
            s = p_move * (p[(i - motion[0]) % len(p)][(j - motion[1]) %
                                                      len(p[i])])
            #failure to move:
            s += (1 - p_move) * p[i][j]
            q[i].append(s)
            
    return q


# Unit 2 Kalman Filters
def f(mu, sigma2, x):
    '''normal probability density'''
    return 1 / sqrt(2.0 * pi * sigma2) * exp(-0.5 * (x - mu) ** 2 / sigma2)

def update(mean1, var1, mean2, var2):
    newMean = (var2*mean1 + var1*mean2) / (var1 + var2)
    newVar = 1 / (1/var1 + 1/var2)
    return [newMean, newVar]

# predict next location given motion
def predict(mean1, var1, mean2, var2):
    #i.e mean2 = intended distance, var2 = error in motion
    newMean = mean1 + mean2
    newVar = var1 + var2
    return [newMean, newVar]

                                
