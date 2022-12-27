        
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
    

def euclid_dist(a,b,c,d):
    return ((a-c)**2+(b-d)**2)**0.5

def solve():
    xa,ya,xb,yb=mii()
    n=ii()
    radiator=[lmii() for i in range(n)]

    cnt =0 

    for y in range(min(ya,yb),max(ya,yb)+1):
        for a,b,c in radiator:
            if euclid_dist(xa,y,a,b)<=c:
                break
        else:
            cnt+=1
    
    for y in range(min(ya,yb),max(ya,yb)+1):
        for a,b,c in radiator:
            if euclid_dist(xb,y,a,b)<=c:
                break
        else:
            cnt+=1

    for x in range(min(xa,xb)+1,max(xa,xb)):
        for a,b,c in radiator:
            if euclid_dist(x,ya,a,b)<=c:
                break
        else:
            cnt+=1

    for x in range(min(xa,xb)+1,max(xa,xb)):
        for a,b,c in radiator:
            if euclid_dist(x,yb,a,b)<=c:
                break
        else:
            cnt+=1

    print(cnt)




    
    
def main():

 
    solve()
 
if __name__ == '__main__':
    main()
    
 


