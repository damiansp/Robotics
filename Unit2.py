#Unit 2

#Kalman Filters
#Update prob distribution given prior and new likelihood Gaussians:

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
