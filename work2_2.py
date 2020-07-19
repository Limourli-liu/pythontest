# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:06:44 2020

@author: Limour
"""
from math import exp,sqrt,pi

def f(x, sigma, mu):
    t = (x-mu)**2
    t /= 2*sigma**2
    t = exp(-t)
    t /= sqrt(2*pi)*sigma
    return t

score = float(input("Please enter the test score of the student:"))
print("The possibility is %f" % (f(score, 8.15, 80)))