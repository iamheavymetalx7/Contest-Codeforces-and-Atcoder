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


'''
helpful problem: https://practice.geeksforgeeks.org/problems/minimum-swaps/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
'''
 
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
    
    
def solve(t):
    n=ii()
    perm=lmii() 

    arr=[]
##################### Same code as the above comment
## Just added vect=[] and few lines to check if i,i+1 lies in the same cycle, after sorting vect arr

    for k,v in enumerate(perm):
        arr.append([k,v])

    arr.sort(key=lambda x:x[1])
    vis=[0]*(n)
    ans=0

    flag=0
    for i in range(n):
        vect=[]
        if vis[i] or arr[i][0]==i:
            continue
        j=i
        cycle_size=0

        while not vis[j]:
            vect.append(arr[j][1])
            vis[j]=1
            j=arr[j][0]
            cycle_size+=1
        vect.sort()
        for j in range(len(vect)):
            if vect[j]==vect[j-1]+1:
                flag=1


        if cycle_size>0:
            ans+=cycle_size-1
    ########## same code till here
    ## then just added depending on the condition !!
    if flag:
        return ans-1
    return ans+1
    
    
def main():
    t = 1
    # if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
    #     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
    #     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
    #     start_time = time.time()
    #     print("--- %s seconds ---" % (time.time() - start_time))
 
 
    # sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        z=solve(i+1)
        print(z)
 
if __name__ == '__main__':
    main()
    
 


