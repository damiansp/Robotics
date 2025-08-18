from __future__ import division
#Unit 2

#Kalman Filters
#Update prob distribution given prior and new likelihood Gaussians:

def f(mu, sigma2, x):
    '''normal probability density'''
    return 1 / sqrt(2.0 * pi * sigma2) * exp(-0.5 * (x - mu) ** 2 / sigma2)

def update(mean1, var1, mean2, var2):
    newMean = (var2*mean1 + var1*mean2) / (var1 + var2)
    newVar = 1 / (1/var1 + 1/var2)
    return [newMean, newVar]

#predict next location given motion
def predict(mean1, var1, mean2, var2):
    #i.e mean2 = intended distance, var2 = error in motion
    newMean = mean1 + mean2
    newVar = var1 + var2
    return [newMean, newVar]


# Example for a series of moves and measurements
measurements = [5, 6, 7, 9, 10]
motion = [1, 1, 2, 1, 1]
measurement_sig = 4
motion_sig = 2
mu = 0
sig = 10000

for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    print [mu, sig]
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)
    print [mu, sig]
                    
