#from heapq import heappop,heappush,heapify #heappop(hq), heapify(list)
#from collections import deque as dq #deque  e.g. myqueue=dq(list)
#append/appendleft/appendright/pop/popleft
#from bisect import bisect as bis #a=[1,3,4,6,7,8] #bis(a,5)-->3
#import bisect #bisect.bisect_left(a,4)-->2 #bisect.bisect(a,4)-->3
#import statistics as stat  # stat.median(a), mode, mean
#from itertools import permutations(p,r)#combinations(p,r)
#combinations(p,r) gives r-length tuples #combinations_with_replacement
#every element can be repeated
        
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

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
   
def solve():
    s1=si()
    s2=si()
    q=0
    final_pos=0
    till_now =0
    for i in range(len(s1)):
        if s1[i]=="+":
            final_pos+=1
        else:
            final_pos-=1
    for i in range(len(s2)):
        if s2[i]=="+":
            till_now+=1
        elif s2[i]=="-":
            till_now-=1
        elif s2[i]=="?":
            q+=1

    t=abs(final_pos-till_now)

    if t>q or (q-t)%2:
        print(0.000000000000)
    else:
        numerator = factorial(q)/(factorial((q-t)//2) * factorial(t+((q-t)//2)))
        denominator = pow(2,q)

        ans = (numerator*1.0)/denominator
        print("{:.11f}".format(ans))


def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
 
    solve()
 
 
if __name__ == '__main__':
    main()
    
 

