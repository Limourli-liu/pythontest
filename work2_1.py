# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:55:39 2020

@author: Limour
"""

from math import *

A = radians(float(input("Please enter the anger A:")))
B = radians(float(input("Please enter the anger B:")))

print("sin(A+B)=%f sinAcosB+cosAsinB=%f"%(sin(A+B), sin(A)*cos(B)+cos(A)*sin(B)))
print("tan(A+B)=%f (tanA+tanB)/(1-tanAtanB)=%f"%(tan(A+B), (tan(A)+tan(B))/(1-tan(A)*tan(B))))
