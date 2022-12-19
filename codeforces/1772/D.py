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

def BinarySearch(low,high,arr,n):
    # print("inside Binary search")
    global x
    flag=0
    if low<=high:
        mid= (low+high)//2

        for i in range(n-1):
            if (abs(arr[i]-mid)>abs(arr[i+1]-mid)):
                if arr[i]>arr[i+1]:
                    flag=1
                else:
                    flag=2
                break
        # print("after for loop..")
        if flag==1:
            BinarySearch(mid+1,high,arr,n)
        elif flag==2:
            BinarySearch(low,mid-1,arr,n)
        else:
            x=mid

    
    
def solve(t):
    n=ii()
    a=lmii()

    global x
    x=-1
    
    low=0
    high = 1000000000

    # print("binary search call...")
    BinarySearch(low,high,a,n)

    print(x)

    
    
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