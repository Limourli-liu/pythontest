'''
有一个子目录zuoye有若干文本文件，gbk编码。分别存储了每个学生提交上来的算术作业，文件名是学生的学号。算术作业包括+-*/，每行一道题。
设计一个自动批改程序，要求完成以下功能：
  允许每个数前后可能有空白
  允许结果为负数的情况
  运算的数均为正整数
  除法只考虑能整除的情况
  要考虑可能有空白行，可能出现在文件的任意位置
  空白行不计入总题数，格式错误的题数计入总题数
  将批改结果保存到文件results.txt，每一行记录
    学号、答对的百分比
'''
import os
import re

dirname = r'D:\ELEARNING\大一下\Python程序设计\Homework\zuoye'
homework = os.listdir(dirname)
suoyou = {}
for h in homework:
    with open(dirname+'\\'+h,'r',encoding='utf-8') as hw:
        eh = hw.readlines()
        eh = [line.strip('\n')for line in eh]
        zq = 0; cw = 0
        for e in eh:
            if e !='':
                e = re.sub(' ','',e)
                t = re.split('=',e)
                try:
                    if eval(t[0])==int(t[1]):
                        zq+=1
                    else:
                        cw+=1
                except:
                    cw+=1
        n = h[0:-4]
        suoyou[n] = 100*(zq/(zq+cw))
        hw.close()
with open(dirname+'\\'+'results.txt','w',encoding='utf-8') as rs:
    for k in suoyou.items():
        s = '%s\t%.2f%%'%(k[0],k[1])
        rs.writelines(s+'\n')
    rs.close()
        
