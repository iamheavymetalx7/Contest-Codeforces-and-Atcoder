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
 
 
si= lambda:str(input())
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')
    
    
if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
    sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
    sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    


for _ in range(ii()):
    a1,a2,a3,a4=mii()

    if a2>a3:
        a2,a3=a3,a2
    ans=0
    if a1==0:
        if a2>0 or a3>0 or a4>0:
            print(1)
        else:
            print(0)
        continue
    ans+=a1

    ans+=2*a2

    a3-=a2

    ans+=min(a1+1,a3+a4)

    print(ans)
    
    
# def solve(t):
    
    
# def main():
#     t = 1
#     if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
#         sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
#         sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
#         start_time = time.time()
#         print("--- %s seconds ---" % (time.time() - start_time))
 
 
#     sys.setrecursionlimit(10**5)
 
#     t = int(input())
 
#     for i in range(t):
#         solve(i+1)
 
 
# if __name__ == '__main__':
#     main()
    
 


