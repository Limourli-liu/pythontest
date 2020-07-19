# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:53:37 2020

@author: Limour
"""

keyl = '大数据、互联网、技术、数据、结构化、处理、难点、分析、很大、合适、平台'.split('、')

def getKey(s):
    for i in range(len(s), 1, -1):#保留1个字
        if s[:i] in keyl:
            return s[:i]
    else:
        return s[0]

s = input('原句子: ')
# s = '互联网大数据技术与分析平台'
# 合适的数据处理平台是大数据技术的重点
# 大数据技术与非结构化数据处理

sp = []
while s:
    sp.append(getKey(s))
    s = s[len(sp[-1]):]

print('切分的结果是:', '/'.join(sp))
