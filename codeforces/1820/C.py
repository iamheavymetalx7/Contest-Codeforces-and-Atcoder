'''
Failed on test case like this:

1
7
0 1 2 3 11 6 7

where mex is 4
and newmex is 5

but we dont have any changes to make using first index and last index
so out newmex is not equal to nmex where nmex is calculated after we change the elements
of the array

good observation i made, but slighly missed, congo !!


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
    n=ii()
    a=lmii()
    b=a.copy()
    b.sort()
    # print(a)
    # print(b)
    mex=0
    for i in range(n):
        if b[i]==mex:
            mex+=1
    # print(mex,"org mex")
    newmex=mex+1
    # print(newmex,"newmex")

    if newmex not in a:
        cnter= Counter(a)
        for key in cnter:
            if cnter[key]>=1 and key>mex:

                print("Yes")
                return
            if cnter[key]>=2 and key<mex:
                print("YES")
                return
        
            


    first_index=n-1
    last_index=0


    for i in range(n-1,-1,-1):
        if a[i]==newmex:
            first_index=i

    for i in range(n):
        if a[i]==newmex:
            last_index=i
    # print(first_index,last_index+1,"this...")

    for j in range(first_index, last_index+1):
        # print(j,"jjj")
        a[j]=mex
    # print(a,len(a),"asda")

    nmex=0

    a.sort()
    for i in range(n):
        if a[i]==nmex:
            nmex+=1
    # print(nmex,newmex)
    if nmex==newmex:
        print("Yes")
        return
    print("No")
    

    
    
    
    
t=ii()
for _ in range(t):
    solve()