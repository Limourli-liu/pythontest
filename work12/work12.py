'''
请将dict.txt和news.txt放在.py的同级目录下
'''

import os

def _path(name, root=None):
    return os.path.join(root or os.getcwd(),name)

with open(_path(r'dict.txt')) as f:
    keyd = {kw.strip('\n'):0 for kw in f}

maxk = max(map(len,keyd))

def _getKey(s):
    for i in range(len(s), 1, -1):#过滤掉长度小于2的单字
        if s[:i] in keyd:
            keyd[s[:i]]+=1
            return i
    else:
        return 1

def _pline(s):
    index_s = 0
    index_e = maxk
    end = len(s) 
    while index_s < end:
        move = _getKey(s[index_s:index_e])
        #print(s[index_s:index_e])
        index_s += move
        index_e += move

with open(_path(r'news.txt')) as f:
    for pg in f:
        pg = pg.strip('\n')
        if pg:
            _pline(pg)


n = int(input('分几列显示? ').strip())
out = sorted(keyd.items(), key = lambda x: x[1], reverse= True)
out = filter(lambda x:x[1], out)
for i,x in enumerate(out):
    if not i%n and i:
        print('\n')
    print(f'　{x[0]:　>{maxk}}:{x[1]:>3}', end='')
