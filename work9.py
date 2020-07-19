'''
输入一个字符串，检查其是否为合法的python变量。输入$$$结束
1. 变量名必须以字母或下划线开始
2. 变量名中不能有空格或标点符号（括号(大中小)、引号、逗号、斜线、反斜线、冒号、句号、问号）
3. 不能使用关键字、函数名等做变量名，定义若干个True False try except break sum min max all any等
对于错误的给出建议：
不符合1的，在变量名前加上一个随机生成的字母；
不符合3的，在变量名最后面加一个随机生成的数字；
不符合2的，将这些符号去除，若去除后，不符合前面两条则按前面两条处理。
'''
import re, random, keyword 
# from random import choice, randint 
#不使用此方式引入random模块 是因为这会将choice和randint引入本模块的方法,与type(input)冲突
w = ''.join(chr(c) for c in range(ord('A'),ord('Z')+1))
w += ''.join(chr(c) for c in range(ord('a'),ord('z')+1))

# r1 = re.compile(r'^(?!\d)\w')#构造条件1
#老师要求必须是字母或下划线开始,其实像"中国"的中开始也是可以的,这时可以用上面一个表达式,即\w可以匹配汉字日文等等
r1 = re.compile(r'^[A-Za-z_]')

r2 = re.compile(r'(?!\w)[\x20-\x7e]')#构造条件2的一部分

r3 = (type(abs),type,type(input)) #构造条件3的一部分
#分别对应内置函数\类\本模块方法

tips = False
def echo(s, t=True):#调试用,请无视
    if tips and t:
        print(s)

def matchr1(s):
    if r1.match(s) is None:
        echo('变量名必须以字母或下划线开始')
        return choice() + s
    return s

def matchr2(s):
    t = True
    if r2.search(s):
        echo('变量名中不能有空格或标点符号',t)
        t = False
        rtn = r2.sub('', s)
    else:
        rtn = s
    
    try:#防止漏网之鱼
        eval(rtn)
    except SyntaxError:
        echo('变量名中不能有空格或标点符号',t)
        rtn = otherc(rtn) #其实不需要正则，直接用这个就行
    finally:
        return rtn

def matchr3(s):
    try:
        if keyword.iskeyword(s):
            echo('不能使用关键字做变量名')
            return s + randint()
        elif isinstance(eval(s),r3) :
            echo('不能使用函数名或类名做变量名')
            return s + randint()
        else:
            # print(eval(f'type({s})'))
            return s
    except Exception:
        return s
def otherc(s):
    rtn = ''
    for c in s:
        try:
            eval(c)
            rtn += c
        except NameError as e:
            if e.args[0][-14:] == 'is not defined':
                rtn += c
        except Exception:
            pass
    return rtn

def choice():
    return random.choice(w)
def randint():
    return str(random.randint(0,9))

def getRight(s):
    rtn = matchr2(s)
    rtn = matchr1(rtn)
    rtn = matchr3(rtn) 
    if rtn == s:
        print('合法.')
    else:
        print(f'建议改为: {rtn}')

while True:
    name = input('请输入一个字符串: ').strip()
    if name != '$$$':
        getRight(name)
    else:
        break

#以下为测试集 在python中变量名含有汉字和日文是合法的 而__name__等虽有特殊含义,但也是可做变量名的
#如未引入re random模块,则此变量名也应认为合理 当然,无论是否引入都是合法的python变量名
r'''
中国 = 1+1
さくら = 'sakura'
abncd
123abcd
abc.9\\3(~o~)
s.u.m
........\\\\
￥￥￥￥。。。aaa哈哈【【。，“”‘’
_￥￥￥￥。。。aaa哈哈【【。，“”‘’
￥￥￥12_3￥。。。aaa哈哈【【。，“”‘’
SyntaxError
Exception
map
str
input
any
lambda
iskeyword
choice
__name__
re
random
try
while
else
import
not
and
$$$
'''
    