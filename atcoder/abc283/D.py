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
    
    
def solve():
    s=si()
    q=deque()
    dict =defaultdict(int)
    A=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for x in A:
        dict[x]=-1
    
    for i in range(len(s)):
        if s[i] in A:
            if dict[s[i]]!=-1:
                print("No")
                break
            else:
                dict[s[i]]=i
        else:
            if s[i]=="(":
                q.append(i)
            else:
                j=q.pop()
                
                for x in A:
                    if j<dict[x]<i:
                        dict[x]=-1
    else:
        print("Yes")
                

    
    
def main():

 
    sys.setrecursionlimit(10**5)
 
 
    solve()
 
 
if __name__ == '__main__':
    main()
    
 
