import sys, threading, os, io 
import math
import time
from os import path
from collections import defaultdict, Counter, deque
from bisect import *

    
def solve():

    s=str(input())
    x=str(input())
    # print(s,x)
    dics = Counter(s)
    dicx = Counter(x)

    f=False

    for key in dics.keys():
        if key in dicx.keys():
            f=True
            break
    
    if not f:
        print("NO")
        return
    
    if s[0]==x[0]:
        print("YES")
        print(s[0]+"*")
        return
    if s[-1]==x[-1]:
        print("YES")
        print("*"+s[-1])
        return


    for i in range(len(s)-1):
        for j in range(len(x)-1):
            if s[i]==x[j] and s[i+1]==x[j+1]:
                print("YES")
                print("*"+s[i]+s[i+1]+"*")
                return
    else:
        print("NO")
        return
 
import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for i in range(t):
    solve()