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
        
#Note direct assignment to check somethings doesnt work always
#say there exists s (list) then ss=s and if we edit ss, it edits s as well
#always try to use ss=s.copy() if u wish to make changes to ss and not reflect them in s.
#For example: see **1379A - Acacius and String** for reference
    
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
 
 
input = lambda: sys.stdin.readline().rstrip(
)
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
    
    
def solve(t):
    n=ii()
    s=si()
    s=list(s)

    change_same=0
    change_diff=0

    if n%2:
        mid = math.ceil(n/2)-1
        i,j=mid-1,mid+1
        while i>=0:
            if s[i]==s[j]:
                if s[i+1]==s[j-1]:
                    i-=1
                    j+=1
                    continue
                else:
                    i-=1
                    j+=1
                    change_same+=1

            else:
                if s[i+1]!=s[j-1]:
                    i-=1
                    j+=1
                    continue
                else:
                    i-=1
                    j+=1
                    change_diff+=1


        


    else:
        mid1,mid2=math.ceil(n//2)-1, math.ceil(n//2)
        if s[mid1]!=s[mid2]:
            change_diff+=1

        i,j=mid1-1, mid2+1
        while i>=0:
            if s[i]==s[j]:
                if s[i+1]==s[j-1]:
                    i-=1
                    j+=1
                    continue
                else:
                    i-=1
                    j+=1
                    change_same+=1

            else:
                if s[i+1]!=s[j-1]:
                    i-=1
                    j+=1
                    continue
                else:
                    i-=1
                    j+=1
                    change_diff+=1

            
            

    
    if change_diff>=2:
        print("No")
        return
    else:
        print("Yes")  
        return 

def main():
    t = 1

 
    t = int(input())
 
    for i in range(t):
        solve(i+1)
 
 
if __name__ == '__main__':
    main()
    
 


