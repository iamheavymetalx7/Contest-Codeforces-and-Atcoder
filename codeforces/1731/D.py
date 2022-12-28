
        
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
 

# https://leetcode.com/problems/maximal-square/solution/
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
 
si= lambda:str(input())
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')

def maxValcheck(arr,mid):
    n=len(arr)
    m=len(arr[0])
    dp=[[0]*m for j in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]>=mid:
                dp[i][j]=1

                if i>0 and j>0:
                    dp[i][j]+=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                if dp[i][j]==mid:
                    return True
    return False

    
    
def solve(t):
    n,m=mii()
    arr=[]
    ans=1
    for i in range(n):
        arr.append(lmii())

    low,high=1,min(m,n)

    while low<=high:
        mid=(low+high)//2
    

        if maxValcheck(arr,mid):
            ans = mid
            low=mid+1
        else:
            high=mid-1
    print(ans)
    
def main():

 
    sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        solve(i+1)
 
 
if __name__ == '__main__':
    main()
    
 


