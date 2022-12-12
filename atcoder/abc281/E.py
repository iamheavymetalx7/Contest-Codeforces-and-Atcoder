import math
import collections
from copy import deepcopy
from collections import defaultdict,deque
from sys import exit,setrecursionlimit
from heapq import heapify,heappush,heappop
from bisect import bisect_left,bisect_right,insort
from itertools import product,permutations,combinations,accumulate,combinations_with_replacement
from decimal import Decimal
from functools import lru_cache
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

# 入力----------------------------------------------------
def II(): return int(input())
def MI(): return map(int, input().split())
def TI(): return tuple(map(int, input().split()))
def LI(): return list(MI())
def MS(): return map(str, input().split())
def LS(): return list(MS())
def LLI(rows): return [LI() for _ in range(rows)]
def LLS(rows): return [list(input()) for _ in range(rows)]
def Graph0(vertex,edge,LLI):
    ret=[[] for _ in range(vertex)]
    for [u,v] in LLI:
        u-=1; v-=1; 
        ret[u].append(v); ret[v].append(u);
    return ret
def Banhei(hight,width,LLS,wall='#'): 
    ret=[[wall]*(width+2)]
    for i in range(hight):
        ret.append([wall]+LLS[i]+[wall])
    ret.append([wall]*(width+2))
    return ret
def MLI(n):  
    arr=LLI(n); l=len(arr[0])
    ret=[[] for _ in range(l)]
    for i in range(n):
        for j in range(l): ret[j].append(arr[i][j])
    return ret

def get_primes(n: int) -> list:
    sieve=[1]*n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [0] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
def gcd(a,b):
    while b!=0: a,b = b,a%b
    return a
def lcm(a,b):
    return(a*b // gcd(a,b))
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return(divisors)
def find_root(root,x):
    y = root[x]
    if x == y: return x
    z = find_root(root,y)
    root[x] = z
    return z
def merge(root,size,x,y):
    x = find_root(root,x)
    y = find_root(root,y)
    if x == y: return
    sx,sy = size[x],size[y]
    if sx < sy:
        sx,sy = sy,sx
        x,y = y,x
    root[y] = x
    size[x] += sy
def getValue(root,size,x):
    return size[find_root(root,x)]
def same(root,x,y):
    return (find_root(root,x)==find_root(root,y))

# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
T = TypeVar('T')

class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans





"""
カンペ
基本的にはSortedSetと同じだが、要素が複数あってもよい。

違う機能
・s.add(x) : xが含まれているかによらず、xを追加
・s.discard(x) : xが含まれていればxを【1個】消し、Trueを返す
※C++のeraseは全部消してしまうので対応する必要があったが、ここでは1個
・s.count(x) : xが何個含まれているかを返す
計算時間はすべてO(sqrt(N))


"""





#E
N,M,K=MI()
A=LI()


ans = sum(sorted(A[:M])[:K])
mu = SortedMultiset(sorted(A[:M]))

ANS=[ans]

if M==K==1:
    print(*A)
    exit()

for i in range(N-M):
    v=0
    if mu[K-1]>=A[i]:
        v+=1
        ans-=A[i]
    mu.discard(A[i])
    if v==0 and mu[K-1]>A[i+M]:
        ans-=mu[K-1]
        ans+=A[i+M]
    elif v==1 and mu[K-1]>A[i+M]:
        ans+=A[i+M]
    elif v==1:
        ans+=mu[K-1]
    mu.add(A[i+M])

    ANS.append(ans)

print(*ANS)






