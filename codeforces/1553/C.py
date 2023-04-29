# /**
# * author:Hisoka-TheMagician
# * created: 29/04/2023 11:09 Chennai, India
# **/
        



'''

The other possible solution is to notice that 
it's optimal to change ? of one team to 
1 and to 0 for other. So you only have two 
candidates to check.

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

    sc0=0
    sc1=0
    ANS=10

    ## converting all question marks for team1 to score
    for i in range(10):
        if i%2==0:
            if s[i]=="1":
                sc0+=1
            elif s[i]=="0":
                True
            else:
                sc0+=1
        else:
            if s[i]=="1":
                sc1+=1
            elif s[i]=="0":
                True
            else:
                True
        
        rest0=(10-(i+1))//2
        rest1=(10-i)//2

        if sc0+rest0<sc1 or sc1+rest1<sc0:
            ANS=min(ANS,i+1)
            break

    sc0=0
    sc1=0

    ## converting all question marks for team2 to score
    for i in range(10):
        if i%2==0:
            if s[i]=="1":
                sc0+=1
            elif s[i]=="0":
                True
            else:
                True
        else:
            if s[i]=="1":
                sc1+=1
            elif s[i]=="0":
                True
            else:
                sc1+=1
        
        rest0=(10-(i+1))//2
        rest1=(10-i)//2

        if sc0+rest0<sc1 or sc1+rest1<sc0:
            ANS=min(ANS,i+1)
            break

    
    print(ANS)


    
    
    
t=ii()
for _ in range(t):
    solve()