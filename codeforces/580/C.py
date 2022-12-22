si= lambda:str(input())
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')
# PYRIVAL BOOTSTRAP
# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/bootstrap.py
from types import GeneratorType
from collections import defaultdict
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc

@bootstrap
def dfs(u,p,numC,maxC,a,graph,m):
    global ans
    if a[u]:
        numC+=1
    else:
        numC=0
    
    maxC=max(maxC,numC)

    numChild=0

    for v in graph[u]:
        if v!=p:
            yield dfs(v,u,numC,maxC,a,graph,m)
            numChild+=1
    
    if numChild==0 and maxC<=m:
        ans+=1
    yield ans

n, m = mii()
a = [0] + lmii()
graph = defaultdict(list)
for i in range(n-1):
    u,v=mii()
    graph[u].append(v)
    graph[v].append(u)

global ans
ans=0
print(dfs(1,-1,0,0,a,graph,m))
