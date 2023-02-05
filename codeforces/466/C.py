#bisect.bisect_left(a, x, lo=0, hi=len(a)) is the analog of std::lower_bound()
#bisect.bisect_right(a, x, lo=0, hi=len(a)) is the analog of std::upper_bound()
#from heapq import heappop,heappush,heapify #heappop(hq), heapify(list)
#from collections import deque as dq #deque  e.g. myqueue=dq(list)
#append/appendleft/appendright/pop/popleft
#from bisect import bisect as bis #a=[1,3,4,6,7,8] #bis(a,5)-->3
#import bisect #bisect.bisect_left(a,4)-->2 #bisect.bisect(a,4)-->3
#import statistics as stat  # stat.median(a), mode, mean
#from itertools import permutations(p,r)#combinations(p,r)
#combinations(p,r) gives r-length tuples #combinations_with_replacement
#every element can be repeated
        
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
 
 
input = lambda: sys.stdin.readline().rstrip(
)
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
    
from collections import Counter
def solve():
    n=ii()
    A=lmii()

    summ=sum(A)

    prefix=[0]*n
    prefix[0]=A[0]
    
    for i in range(1,n):
        prefix[i]=prefix[i-1]+A[i]
    
    arr=[]
    if summ%3==0:
        cntsumby3=0
        cntsumby3_2=0
        s1=0
        for i in range(n-1):
            s1+=A[i]

            if s1== 2*(summ//3):
                cntsumby3_2+=cntsumby3

            if s1==summ//3:
                cntsumby3+=1

        print(cntsumby3_2)



    else:
        print(0)



def main():
    # t = 1
    # if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
    #     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
    #     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
    #     start_time = time.time()
    #     print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
 
    solve()
 
 
if __name__ == '__main__':
    main()
    
 


