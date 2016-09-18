###########################
#                         #
#  Sampling with weights  #
#                         #
###########################

from math import *
import random

p = ['a', 'b', 'c', 'd', 'e']

w = [1., 2., 3., 4., 5.]
w_norm = []

for i in range(len(w)):
    w_norm.append(w[i] / sum(w))

w_norm_cum = []

for i in range(len(w_norm)):
    w_norm_cum.append(sum(w_norm[:i]))


p3 = []     #place holder for resampled particles


for j in range(len(p)):
    #generate uniform rn:
    rv = random.uniform(0, 1)
    rv_match = 0
    
    #determine which particle it corresponds to:
    for i in range(len(w_norm_cum)):
        if rv > w_norm_cum[i]:
            rv_match = i + 1

    if rv_match > i:
        rv_match = i
            
    #sample the particle with the matching index:
    p3.append(p[rv_match])

    
