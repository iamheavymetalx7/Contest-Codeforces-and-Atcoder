# /**
# * author:Hisoka-TheMagician
# * created: 02/05/2023 14:02 Chennai, India
# **/
        

'''
Editorial :


Let's start with an array where every single bit in every single 
element is 1. It clearly doesn't have bitwise-and
equal to 0, so for each bit, we need to turn it off 
(make it 0) in at least one of the elements.

However, we can't turn it off in more than one element,
since the sum would then decrease for no reason. 
So for every bit, we should choose exactly 
one element and turn it off there. Since there are k
bits and n
elements, the answer is just n**k
.


'''    
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
    
    
# if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
#     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
#     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    
def solve():
    mod=10**9+7
    n,k=mii()
    print(pow(n,k,mod))

t=ii()
for _ in range(t):
    solve()