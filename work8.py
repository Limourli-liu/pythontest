'''
有一些参考文献的格式如下：
文献名称. 文献来源-会议, 年份, 页面范围.
或
文献名称. 文献来源-期刊, 年份,卷(期):页面范围.

文献和文献来源中间有一个空格,  文献名称、来源都不含.,
对于会议文献，年份和页面中间也有空格。
对于期刊文献，年份、卷、期和页面中间没有空格

A large scale study of web password habits. The International Conference on WWW, 2007, 657-666.
On user choice in graphical password schemes. The 13th USENIX Security Symposium, 2004, 15-28.
The Pollyanna hypothesis. Journal of Verbal and Learning Behavior, 1969,8(1):1-8.
Support Vector Machine. Journal of Machine Learning, 1992,8(12):110-119.

  
要求，提取文献名称，文献来源，分年，页面范围。 如果是期刊的话，还需要提取卷、期
'''

import re

def count():
    n = 1
    while True:
        yield n
        n+=1        
counter = count()

d = '''A large scale study of web password habits. The International Conference on WWW, 2007, 657-666.
On user choice in graphical password schemes. The 13th USENIX Security Symposium, 2004, 15-28.
The Pollyanna hypothesis. Journal of Verbal and Learning Behavior, 1969,8(1):1-8.
Support Vector Machine. Journal of Machine Learning, 1992,8(12):110-119.'''

mt = re.compile(r'([\w ]+)\. ([\w ]+)\, (\d+)\, (\d+)-(\d+)\.')
jn = re.compile(r'([\w ]+)\. ([\w ]+)\, (\d+)\,(\d+)\((\d+?)\):(\d+)-(\d+)\.')

print(*[f'''****文献{next(counter)}****
名称: {name}
会议名称: {meeting}
年份: {date}
开始页号: {start}
终止页号: {end}''' for name, meeting, date, start, end in mt.findall(d)], sep='\n')

print(*[f'''****文献{next(counter)}****
名称: {name}
期刊名称: {journal}
年份: {date}
卷: {volume}
期: {issue}
开始页号: {start}
终止页号: {end}''' for name, journal, date, volume, issue, start, end in jn.findall(d)], sep='\n')