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
from collections import Counter


def to_return(n,A):
    C=Counter(A)

    if max(C.values())>2:
        return

    B=[[] for i in range(n+1)]

    for k,v in enumerate(A):
        B[v].append(k)

    P=[None]*n
    Q=[None]*n        

    # print(B)

    hidden=[]

    for i in range(n,0,-1):
        vis=B[i]

        if len(vis)==0:
            if len(hidden)==0: return
            u,v=hidden.pop() #v,u
            P[u],Q[v]=i,i    
        
        elif len(vis)==2:
            u,v=vis
            P[u],Q[v]=i,i
            hidden.append((v,u))
        
        else:
            u=vis[0]
            P[u]=Q[u]=i
    return P,Q





def solve(t):
    n=ii()
    A=lmii()


    ans = to_return(n,A)

    if ans==None:
        print("NO")
    else:
        print("YES")
        P,Q=ans
        print(*P)
        print(*Q)
     






'''
5
1
1
5
5 3 4 2 5
2
1 1
5
5 3 4 3 5
6
1 2 6 6 4 4
'''
    
    
    
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
    
 


