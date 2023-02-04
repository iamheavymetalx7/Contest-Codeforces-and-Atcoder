#bisect.bisect_left(a, x, lo=0, hi=len(a)) is the analog of std::lower_bound()
#bisect.bisect_right(a, x, lo=0, hi=len(a)) is the analog of std::upper_bound()
#from heapq import heappop,heappush,heapify #heappop(hq), heapify(list)
#from collections import deque as dq #deque  e.g. myqueue=dq(list)
#append/appendleft/appendright/pop/popleft
#from bisect import bisect as bis #a=[1,3,4,6,7,8] #bis(a,5)-->3
#import bisect #bisect.bisect_left(a,4)-->2 #bisect.bisect(a,4)-->3
#import statistics as stat  # stat.median(a), mode, mean
#from itertools import permutations(p,r)#combinations(p,r)
#combinations(p,r) gives r-length tuples #combinations_with_replacement
#every element can be repeated
        
import sys, threading, os, io 
import math
import time
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
import bisect
from io import BytesIO, IOBase								


def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 

input = lambda: sys.stdin.readline().rstrip("\r\n")

def lmii():
    return list(map(int,input().split()))

def ii():
    return int(input())

def si():
    return str(input())
    
def lmsi():
    return list(map(str,input().split()))
    
def mii():
    return map(int,input().split())

def msi():
    return map(str,input().split())

i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')


#####################################################


class SortedList():
        BUCKET_RATIO = 50
        REBUILD_RATIO = 170
    
        def __init__(self,buckets):
            buckets = list(buckets)
            buckets = sorted(buckets)
            self._build(buckets)
    
        def __iter__(self):
            for i in self.buckets:
                for j in i: yield j
    
        def __reversed__(self):
            for i in reversed(self.buckets):
                for j in reversed(i): yield j
    
        def __len__(self):
            return self.size
    
        def __contains__(self,x):
            if self.size == 0: return False
            bucket = self._find_bucket(x)
            i = bisect.bisect_left(bucket,x)
            return i != len(bucket) and bucket[i] == x
    
        def __getitem__(self,x):
            if x < 0: x += self.size
            if x < 0: raise IndexError
            for i in self.buckets:
                if x < len(i): return i[x]
                x -= len(i)
            raise IndexError
    
        def _build(self,buckets=None):
            if buckets is None: buckets = list(self)
            self.size = len(buckets)
            bucket_size = int(math.ceil(math.sqrt(self.size/self.BUCKET_RATIO)))
            tmp = []
            for i in range(bucket_size):
                t = buckets[(self.size*i)//bucket_size:(self.size*(i+1))//bucket_size]
                tmp.append(t)
            self.buckets = tmp
    
        def _find_bucket(self,x):
            for i in self.buckets:
                if x <= i[-1]:
                    return i
            return i
    
        def add(self,x):
            # O(√N)
            if self.size == 0:
                self.buckets = [[x]]
                self.size = 1
                return True
    
            bucket = self._find_bucket(x)
            bisect.insort(bucket,x)
            self.size += 1
            if len(bucket) > len(self.buckets) * self.REBUILD_RATIO:
                self._build()
            return True
    
        def remove(self,x):
            # O(√N)
            if self.size == 0: return False
            bucket = self._find_bucket(x)
            i = bisect.bisect_left(bucket,x)
            if i == len(bucket) or bucket[i] != x: return False
            bucket.pop(i)
            self.size -= 1
            if len(bucket) == 0: self._build()
            return True
    
        def lt(self,x):
            # less than < x
            for i in reversed(self.buckets):
                if i[0] < x:
                    return i[bisect.bisect_left(i,x) - 1]
    
        def le(self,x):
            # less than or equal to <= x
            for i in reversed(self.buckets):
                if i[0] <= x:
                    return i[bisect.bisect_right(i,x) - 1]
    
        def gt(self,x):
            # greater than > x
            for i in self.buckets:
                if i[-1] > x:
                    return i[bisect.bisect_right(i,x)]
    
        def ge(self,x):
            # greater than or equal to >= x
            for i in self.buckets:
                if i[-1] >= x:
                    return i[bisect.bisect_left(i,x)]
        def index(self,x):
            # the number of elements < x
            ans = 0
            for i in self.buckets:
                if i[-1] >= x:
                    return ans + bisect.bisect_left(i,x)
                ans += len(i)
            return ans
    
        def index_right(self,x):
            # the number of elements < x
            ans = 0
            for i in self.buckets:
                if i[-1] > x:
                    return ans + bisect.bisect_right(i,x)
                ans += len(i)
            return ans
 
 

#########################################
    
    
if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
    sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
    sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    

for _ in range(ii()):
    n,q=mii()
    A=lmii()


    h=SortedList([i+1 for i in range(n)])

    dic=defaultdict(int)
    for i in range(n):
        dic[i+1]=0


    for _ in range(q):
        mi=lmii()
        if len(mi)==3:
            val,left,right=mi
            ind = h.index(left)

            while ind<len(h) and h[ind]>=left and h[ind]<=right:
                if dic[h[ind]]<=2:
                    dic[h[ind]]+=1

                    snum=A[h[ind]-1]
                    
                    A[h[ind]-1]= sum(int(el) for el in str(snum))

                    ind+=1
                else:
                    h.remove(h[ind])

        else:
            val,x=mi
            print(A[x-1])



# def solve(t):
    

    