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
 
 
input = lambda: sys.stdin.readline().rstrip()
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
    

from collections import Counter 

"""
The key thing to notice in this task is, 
if we can arrange the characters of 
the string we have into a palindrome,
then there can be at most one character
with an odd amount of occurences. 
This easily gives us the answer: 
if there are <= 1 characters with an 
odd amount of occurences in the initial 
string, then the winner is the first player.
Otherwise, the answer is dependant on 
whether the amount of characters with 
odd amounts of occurences is even or odd; 
if it's even then the second player wins, 
otherwise the first player wins (since the 
one who is forced to get this amount to one 
first is going to lose).

"""
def solve():
    s=si()
    dic=Counter(s)
    cnt_odd=0
    for k,v in dic.items():
        if dic[k]%2:
            cnt_odd+=1
    if cnt_odd<=1:
        print("First")
        return
    if cnt_odd%2:
        print("First")
        return
    else:
        print("Second")
        return
    
    
    
solve()  
# t=ii()
# for _ in range(t):
#     solve()