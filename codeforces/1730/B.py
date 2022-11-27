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
 

def intersect(a,b):
    if a[1]<b[0]:
        return [-1,-1]
    return [max(a[0],b[0]),min(a[1],b[1])]

 
def solve(t):
    n=int(input())
    x=list(map(int, input().split()))
    t=list(map(int, input().split()))

    low, high=0, pow(10,9)+5
    ans=0
    iters=50
##when we have doubles / decimals involved doinf
## while(low<=high) can run in infinite loop, better to use
# number of iterations
    while(iters>0):
        mid=(low+high)/2
        ok=1
        full=[0,pow(10,9)+5]

        for i in range(n):
            if t[i]>mid:
                ok=0
                break

            diff=mid-t[i]
            segment=[x[i]-diff,x[i]+diff]

            full=intersect(segment,full)

            if full[0]==-1:
                ok=0
                break
        
        if ok:
            ans=(full[0]+full[1])/2
            high=mid
        else:
            low=mid
        
        iters-=1
    print(round(ans,12))


 
##Then people will be 
# able to meet only if 
# these segments intersect, 
# that is, the minimum of the
#  right borders is greater than or
#  equal to the maximum of the left
#  borders.  

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