# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:45:59 2020

@author: Limour

例2:
输入乘法（任意位数的整数，整数前后允许加入任意个空格）运算表达式，程序判断对错。
15*5=75     正确！
3*123=369   正确！
15 * 20 = 300  正确
10*200=200 错误
ab*20=2001 不是一个合法的乘法运算~
20*31=62i  不是一个合法的乘法运算~
15+20=35  不是一个乘法运算！
3*2   不是一个完整的乘法运算！

将例2拓展到加减乘除运算，其中除法按小数点后面两位为精度。

提示"请输入一个四则运算式："，输入时可能包含空格、字母、数字等，判断算式是否正确。判断规则如下：
没有= "不是一个完整的算式！"
没有+-*或/ "不是一个四则运算！"
三个数存在不合法的 "不是一个合法的四则运算~"
（其中，对于除法假设用户输入答案是一个合法的数）
除法运算/0 "除数为0."
算式正确 "正确！"
算式错误 "错误."
"""
from decimal import Decimal
opset = {'+', '-', '*', '/'}
expr = input('请输入一个四则运算式：')
if any(c in opset for c in expr):
    oppos, eqpos = -1, -1
    for i in range(len(expr)):
        if expr[i] in opset:
            oppos = i
        elif expr[i] == '=':
            eqpos = i
            break #找到等于就不必再找了
    else: #没找到等于
        print('不是一个完整的算式！')
    # print(oppos, eqpos)
    if -1 < oppos < eqpos:#n1 op n2 = n3
        n1 = expr[:oppos].strip()
        op = expr[oppos]
        n2 = expr[oppos+1:eqpos].strip()
        n3 = expr[eqpos+1:].strip()
        # print(n1, op, n2, n3)
        if n1.isnumeric() and n2.isnumeric() and (op == '/' or n3.isnumeric()):#忽略负数
            if op == '+':
                print("正确！" if int(n1)+int(n2) == int(n3) else "错误.")
            elif op == '-':
                print("正确！" if int(n1)-int(n2) == int(n3) else "错误.")
            elif op == '*':
                print("正确！" if int(n1)*int(n2) == int(n3) else "错误.")
            else:
                n1, n2, n3 = Decimal(n1), Decimal(n2), Decimal(n3)
                if n2.is_zero():
                    print ("除数为0.")
                else:
                    ans = (n1 / n2).quantize(n3, rounding = 'ROUND_HALF_UP')#默认输入答案是格式正确的
                    print("正确！" if n3 == ans else "错误.")
        else:
            print('不是一个合法的四则运算~')
    # elif eqpos != -1: #不考虑这种情况
    #     print('请将结果写在算式右边!')
else:
    print('不是一个四则运算！')
    
    
    