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
        
import sys, threading
import math
import time
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
 
 
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
alphs = "abcdefghijklmnopqrstuvwxyz"
 
    
def solve():
    n,m,k=mii()
    #x is the euclidean distance
    #n rows
    #m cols
    keyboard = [si() for x in range(n)]
    q=ii()
    string=si()

    map={}
    shifts=[]

    for i in range(n):
        for j in range(m):
            if keyboard[i][j]=="S":
                shifts.append([i,j])

    Capitalize ={}

    for alph in alphs:
        Capitalize[alph]=False
    
    for i in range(n):
        for j in range(m):
            now=keyboard[i][j]
            if now=="S": continue
            map[now]=True

            for y in shifts:
                if (i-y[0])**2+(j-y[1])**2<=k**2:
                    Capitalize[now]=True
                    break
    count=0
    for j in string:
        if map.get(j.lower())==None:
            return -1
        if j!=j.lower():
            if len(shifts)==0:
                return -1
            if Capitalize[j.lower()]==False:
                count+=1
    return(count)



def main():

    z=solve()
    print(z)
 
if __name__ == '__main__':
    main()
    
 


