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
    
    

m,s=mii()

sum=s

if m==1 and s==0:
    print(0,0)
    exit(0)
if m*9<s or s==0:
    print(-1,-1)
    exit(0)

cnt1=s
cnt2=s

ans1=""
ans2=""

for i in range(m):
    if cnt2>=9:
        ans2+="9"
        cnt2-=9
    else:
        ans2+=str(cnt2)
        cnt2=0
    
for i in range(m-1,0,-1): ## taking 1 digits less here
    if cnt1>9:
        ans1+="9"
        cnt1-=9
    else:
        ans1+=str(cnt1-1)
        cnt1=1
ans1+=str(max(1,cnt1))

print(ans1[::-1],ans2)







    
 


