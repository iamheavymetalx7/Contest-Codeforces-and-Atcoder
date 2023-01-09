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
from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound
 
from io import BytesIO, IOBase

# # # # # # # # # # # # # # # #
#       JAI SHREE RAM         #
# # # # # # # # # # # # # # # #
 
 
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
 
si= lambda:str(input())
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')


# # # # # # # # # # # # # # Segment Tree # # # # # # # #
from math import gcd
# Change the function to GCD since we are interested in calculating gcd for the subarrays..
#-------------------------------------------------------------------------
 
class SegmentTree:
    def __init__(self, data, default=0, func=gcd):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
 
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])
        
 
    def __delitem__(self, idx):
        self[idx] = self._default
 
    def __getitem__(self, idx):
        return self.data[idx + self._size]
 
    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1
 
    def __len__(self):
        return self._len
 
    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size
 
        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1
 
        return self._func(res_left, res_right)
 
    def __repr__(self):
        return "SegmentTree({0})".format(self.data)
       
#-------------------------------------------------------------------------
 
if(os.path.exists('/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt')):
    sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt","r") ; sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt","w") 
    start_time = time.time()
    # print("--- %s seconds ---" % (time.time() - start_time))
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = ii()
s = lmii()
d = defaultdict(lambda:[])
for i in range(n):
    d[s[i]].append(i)

def cnt(x,left,right):
    l = bisect_left(d[x],left)
    r = bisect_right(d[x],right)
    return r-l



seg = SegmentTree(s)
for _ in range(ii()):
    l,r = lmii()
    l-=1
    r-=1
    g = seg.query(l,r+1)
    # print(s[l:r])
    # print(g,"gcd")
    print(r-l+1-cnt(g,l,r))




    
# def main():

    
#     solve()


# if __name__ == '__main__':
#     main()
    
 


