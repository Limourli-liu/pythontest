# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:31:21 2020

@author: Limour
"""

n = input('Please input the number:')
if not 99 < int(n) <= 999:
    print('E:The number is illegal')
else:
    print(f'''the first number is {n[2]}
the second number is {n[1]}
the third number is {n[0]}''')
    print("max number is %d and min number is %d"%(int(max(n)),int(min(n))))