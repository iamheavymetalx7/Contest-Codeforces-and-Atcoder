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
 
def solve(t):

    flag = 0

    n,x=map(int, input().split())
    a=[-1]*(n+1)
    vis=[False]*(n+1)

    a[1],a[n]=x,1
    vis[1]=True
    vis[x]=True

    for i in range(2,n):
        for j in range(i,n+1,i): ##this
            if not vis[j] and i==j:
                a[i]=j
                vis[j]=True
                break ##breaking this for loop
            elif not vis[j] and n%j==0:
                a[i]=j
                vis[j]=True
                break ##breaking this for loop
        if a[i]==-1:
            flag=1
        
    if flag==1:
        print(-1)
    else:
        print(*a[1:])






def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        solve(i+1)
 
 
if __name__ == '__main__':
    main()




