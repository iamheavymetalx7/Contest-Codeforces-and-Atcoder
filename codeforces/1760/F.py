##
import sys, threading
import math
import time
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
#By atg_coder27, contest: Codeforces Round #835 (Div. 4), problem: (F) Quests, Accepted, #, Copy
 
# # # # # # # # # # # # # # # #
#       JAI SHREE RAM         #
# # # # # # # # # # # # # # # #
 
 
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
def findmaxk(l,r,a,c,d):
    while l<=r:
        mid=(r+l)//2

        if check(a,mid,c,d):
            ans=mid
            l=mid+1
        else:
            r=mid-1
    return ans

def check(a,k,c,d):
    n=len(a)
    k=k+1
    if k<=n:
        sub=a[:k]
    else:
        sub=list(a)
        for i in range(k-n):
            sub.append(0)

    time=d//k
    cur_sum = time*sum(sub)

    d%=k

    for i in range(d):
        cur_sum+=sub[i]

    return cur_sum>=c




def solve(t):
    n, c, d = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    cummul = [0]*n
    cummul[0] = a[0]
    for i in range(1, n):
        cummul[i] = cummul[i-1] + a[i]
    if sum(a[:d]) >= c:
        print('Infinity')
        return
    if a[0]*d < c:
        print('Impossible')
        return
    print(findmaxk(0,d+10,a,c,d))




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