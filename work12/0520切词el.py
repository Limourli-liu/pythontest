'''
请将news、dict文件与作业文件放在统一目录中
'''
import os
from collections import Counter

dic=[]
loc=os.getcwd() #获取当前文件路径
with open(loc+'//'+'news.txt') as n,open(loc+'//'+'dict.txt') as d:
    news=''.join(n.readlines()) #新闻文本，字符串格式
    dic0=d.readlines()  
    for line in dic0:
        line=line.strip('\n') 
        dic.append(line)    #字典文本，列表格式
    n.close
    d.close

def qc(x,y): #切词函数
    r=[]
    for i in range(len(x)): #循环,切片
        a=x
        while a not in y and len(x)>1:
            if len(a)==2:
                r.append(a[0])
                a=x[1:]
                x=x[1:]
            else:
                a=a[:-1]
        r.append(a) 
        x=x[len(a):]

        if len(x)==0 : #break condition
             break
    return r

def fil(x): #筛选函数
    if len(x)>1 and x!='\u3000' and x!='\n':
        return True
    
res=list(filter(fil,qc(news,dic))) #筛选后的结果

result = Counter(res) #统计词频
px = sorted(result.items(), key=lambda x: x[1], reverse=True) #排序

col=int(input('分几列显示？')) #分列显示
for i in range(len(px)):
    print('{}:{}'.format(px[i][0].ljust(4),str(px[i][1]).ljust(2)),end='  ') #努力对齐qaq
    if (i+1)%col==0:
        print('\n')
