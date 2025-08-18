#!/usr/bin/env python
from __future__ import division
from math import *


def f(mu, sigma2, x):
    '''normal probability density'''
    return 1 / sqrt(2.0 * pi * sigma2) * exp(-0.5 * (x - mu) ** 2 / sigma2)



def update(mean1, var1, mean2, var2):
    '''Given prior with mean1 and var1, likelihood measurement with mean2, var 2,
    calculate posterior mean and var'''
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1 / ((1 / var1) + (1 / var2))
    return [new_mean, new_var]



def predict(mean1, var1, mean2, var2):
    '''Given prior (location prob) with mean1, var1, and a movement of distance mean2,
    and uncertainty var2, calculate posterior'''
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

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

