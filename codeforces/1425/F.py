# /**
# * author:Hisoka-TheMagician
# * created: 05/05/2023 13:06 Chennai, India
# **/
        

    
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

from sys import stdout
n=ii()

a=[0]*(n+1)

print("? 1 2")
stdout.flush()
val1=ii()

print("? 2 3")
stdout.flush()
val2=ii()

print("? 1 3")
stdout.flush()
val3=ii()

a[3]=val3-val1
a[1]=val3-val2
a[2]=val1-a[1]
for i in range(3,n):
    print("?"+" "+str(i)+" "+str(i+1))
    stdout.flush()

    vall = ii()
    a[i+1] = vall-a[i]


print("!", ' '.join(map(str, a[1:])),flush=1)
print(flush=1)
