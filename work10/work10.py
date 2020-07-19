import os, re
r = re.compile(r'^([\d\+\-\*/\(\)]+)=([\d\+\-\*/\(\)]+)$')
rc = re.compile(r'[\s]+')

try:
    from tqdm import tqdm #想知道有什么用请 pip install tqdm
except ModuleNotFoundError:
    def tqdm(iter,*arg,**kw):
        return iter

def _path(name, root=None):
    p =  os.path.join(root or os.getcwd(),name)
    return (os.path.exists(p) or not os.mkdir(p)) and p

def _listdir(name):
    p = _path(name)
    return [os.path.join(p,f) for f in os.listdir(p)]

def _sID(p):
    filepath,fullflname = os.path.split(p)
    fname,ext = os.path.splitext(fullflname)
    return fname

def isRight(expression):
    try:
        match = r.findall(expression)
        if len(match) != 1:
            return False
        left, right = match[0]
        return eval(left) == eval(right)
    except Exception:
        return False
    

def process(f):
    total = correct = 0
    for expression in f:
        mexp = rc.sub('',expression)
        if mexp:
            correct += isRight(mexp)
            total += 1
        else:
            continue
    if total:
        return _sID(f.name) + f' {correct/total}'
    else:
        return _sID(f.name) + ' 0/0'
    

with open(os.path.join(os.getcwd(), r'results.txt'), 'w') as result:
    for f in tqdm(_listdir(r'zuoye'), ncols=80, desc='处理进度'):
        with open(f, 'r', encoding='gbk') as file:
            result.write(process(file)+'\n')
        