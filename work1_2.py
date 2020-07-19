# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:28:37 2020

@author: Limour
"""

n = input('Please input the number:')
if not 99 < int(n) <= 999:
    print('E:The number is illegal')
else:
    nlist = (int(n[2]), int(n[1]), int(n[0]))
    aver = round(sum(nlist)/3, 2)
    print("average is %.2f"%aver)
    for i in nlist:
        if i > aver:
            staus = 'greater than'
        elif i < aver:
            staus = 'less than'
        else:
            staus = 'equal to'
        print("%d is %s %.2f"%(i,staus,aver))
        
