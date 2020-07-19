# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:11:46 2020

@author: Limour
"""
def enURL(s, encoding = 'gbk'):
    return ''.join(chr(b) if b < 128 else '%%%X'%b for b in s.encode(encoding))

key1 = enURL('Python爬虫大数据')
key3 = enURL('清华大学出版社')

print (f'http://search.dangdang.com/?medium=01&key1={key1}&key3={key3}&category_path=01.00.00.00.00.00')
