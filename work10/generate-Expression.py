import os, random, itertools
Nested = 20

try:
    from tqdm import tqdm #想知道有什么用请 pip install tqdm
except ModuleNotFoundError:
    def tqdm(iter,*arg,**kw):
        return iter

def _path(name, root=None):
    p =  os.path.join(root or os.getcwd(),name)
    return (os.path.exists(p) or not os.mkdir(p)) and p

def _prime_l(p):
    return lambda x:x%p

def _prime():
    yield 2
    n = itertools.count(3,2)
    while True:
        p = next(n)
        yield p
        n = filter(_prime_l(p), n)

def _fact(n):
    factor = set()
    pl = _prime()
    while n != 1:
        p = next(pl)
        while not n%p:
            factor.add(p)
            n //= p
    return factor

def randint(n = 99):
    return random.randint(1,n)

def _add(m, ev, n):
    if ev >= n:
        return m, ev
    r = randint(n - ev)
    if randint() < Nested:
        if randint() < 50:
            return f'{r}+{m}', ev + r
        return f'{m}+{r}', ev + r
    om, oev = op(r, r, n - ev)
    if randint() < 50:
        return f'{om}+{m}', ev + oev
    return f'{m}+{om}', ev + oev

def _d(m):
    return m if isinstance(m, int) or m.isdigit() else f'({m})'

def _sub(m, ev, n):
    if ev <= 1:
        return m, ev
    r = randint(ev - 1)
    if randint() < Nested:
        return f'{m}-{r}', ev - r
    om, oev = op(r, r, ev - 1)
    return f'{m}-{_d(om)}', ev - oev

def _mul(m, ev, n):
    if n // ev <= 1:
        return m, ev 
    r = random.randint(2, n // ev)
    if str(m) == '1':
        return r, r
    if randint() < Nested:
        if randint() < 50:
            return f'{r}*{_d(m)}', ev*r
        return f'{_d(m)}*{r}', ev*r
    om, oev = op(r, r, n // ev)   
    if randint() < 50:
        return f'{_d(om)}*{_d(m)}', ev*oev
    return f'{_d(m)}*{_d(om)}', ev*oev

def _dev(m, ev, n):
    if ev <= 1:
        return m, ev
    r = random.choice(list(_fact(ev)))
    return f'{_d(m)}/{r}', ev // r

opset = (_add, _sub, _mul, _dev)
def _op(m, ev, n):
    return random.choice(opset)(m, ev, n)
def op(m, ev, n):
    return _op(*_op(m, ev, n),n)
    
def mexp(Correct_rate = 50):
    r = randint()
    m, ev = op(*op(r, r, 999),9999)
    return f'{m}={ev if random.randint(0, Correct_rate) else randint(9999)}'

izy = \
['''
5+9=14
67-10=57
80-90=-10
70*2=10
5+2=7
67- 9=50
89-10=79
34*3= 102
''',
'''
15+9=24
65-10=55
70-90=-10
70*2=140
5+2=7
90/9=10
80/16=5
''',
'''
12/4=3

15-9=6
25+10=35
70+90=160
70*2=140
5+2=7
90-70=20
76-a=76
''']

with open(os.path.join(_path(r'zuoye'),r'1002131.txt'), 'w') as f:
    f.write(izy[0])
with open(os.path.join(_path(r'zuoye'),r'1002132.txt'), 'w') as f:
    f.write(izy[1])
with open(os.path.join(_path(r'zuoye'),r'1002133.txt'), 'w') as f:
    f.write(izy[2])

for id in tqdm(range(1002134, 1002230), ncols=80, desc='生成进度'):
    with open(os.path.join(_path(r'zuoye'),str(id)), 'w') as f:
        for i in range(random.randint(100, 200)):
            f.write((mexp() if random.randint(0,9) else '') + '\n')