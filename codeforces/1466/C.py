# /**
# * author:Hisoka-TheMagician
# * created: 02/05/2023 19:45 Chennai, India
# **/
        



'''
EDITORIAL HINT:
The main observation is that if there exists a 
palindrome of length larger than 3, then there 
exists a palindrome of length 2 or 3.
This observation allows us to simplify 
the task to erasing all palindromes of length 2 or 3.
We can also notice that each character 
will be replaced at most once.
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
    s=si()
    n=len(s)
    used=[0]*n
    ans=0

    for i in range(1,n):
        use_need=0
        if s[i]==s[i-1] and not used[i-1]:
            use_need=1
        
        if i>1 and s[i]==s[i-2] and not used[i-2]:
            use_need=1
        used[i]=use_need
        ans+=used[i]
    print(ans)

    
    
    
    
t=ii()
for _ in range(t):
    solve()