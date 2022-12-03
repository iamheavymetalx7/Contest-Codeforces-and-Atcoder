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
 
#AtCoder Assemble

def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
 
si= lambda:str(input())
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')



	    
		


    
def solve():
    N=ii()
    c=Counter()
    ans=1
    for i in range(2,int(math.sqrt(N))+1,1):
        while N % i== 0:
            c[int(i)]+=1
            N//=i

        a=c[i]
        n=0
        while a>0:
            n+=i
            x=n
            while x%i==0:
                x//=i
                a-=1
        ans=max(ans,n)

    ans=max(ans,N)

    return ans



def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/input.txt"):
  
        sys.stdout = open('/Users/nitishkumar/Documents/Template_Codes/Python/CP/AtCoder/output.txt','w')
        sys.stdin = open('/Users/nitishkumar/Documents/Template_Codes/Python/CP/AtCoder/input.txt','r')

        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
    z=solve()
    print(z)
 
if __name__ == '__main__':
    main()