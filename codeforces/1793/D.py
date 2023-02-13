
    
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


n=ii()
p=lmii()
q=lmii()

pos_p = [0]*(n+1)
pos_q = [0]*(n+1)

for i in range(n):
    pos_p[p[i]]=i+1
    pos_q[q[i]]=i+1



left=min(pos_p[1],pos_q[1])
right=max(pos_p[1],pos_q[1])

ans=0

ans+= ((left-1)*(left))/2

ans+=((n-right)*(n-right+1))/2

diff = (right-left-1)

ans+=(diff*(diff+1))/2


for i in range(2,n+1):

    a=min(pos_p[i],pos_q[i])
    b=max(pos_p[i],pos_q[i])

    ## b>a always true!!
    canLeft,canRight=0,0

    if b<left:
        canLeft = left-b
        canRight = n+1-right
    
    elif a>right:
        canLeft=left
        canRight = a-right
    
    elif b>right and a<left:
        canLeft=left-a
        canRight = b- right

    ans+=canLeft*canRight
    
    # print(i)
    left=min(left,pos_p[i],pos_q[i])
    right=max(right,pos_p[i],pos_q[i])

ans+=1 ## for the whole permutation case


print(int(ans))



