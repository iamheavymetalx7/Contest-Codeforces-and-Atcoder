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
    
    
# if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
#     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
#     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
# source code: https://codeforces.com/contest/1781/submission/189556202


for _ in range(ii()):
    n=ii()
    s=si()

    count = [[0,i] for i in range(26)]  #since there are 26 characters

    for i in range(n):
        count[(ord(s[i])-97)][0]+=1
    
    count.sort(reverse=True)    #sorting by most freq appeared char 


    answer = math.inf
    best_uniq_char = -1
    best_each_count = -1

    for uniq_char in range(1,27):
        if n%uniq_char!=0:
            continue

        each_count = n//uniq_char


        temp=0

        for i in range(26):
            if count[i][0] > each_count:
                temp+=count[i][0]-each_count
            elif i>=uniq_char:
                temp+=count[i][0]
        
        if temp<answer:
            answer=temp
            best_each_count=each_count
            best_uniq_char=uniq_char
    
    target =[0]*26

    for i in range(best_uniq_char):
        target[count[i][1]]=best_each_count
    
    ## making of the string

    answer_s=['']*n
    count2=[0]*26

    for i in range(n):
        if count2[ord(s[i])-97]<target[ord(s[i])-97]:
            answer_s[i]=s[i]
            count2[ord(s[i])-97]+=1

    # print(answer_s)
    pointer_c=0
    pointer_s=0


    while True:
        while pointer_c<26 and count2[pointer_c]==target[pointer_c]:
            pointer_c+=1

        if pointer_c==26:
            break

        while pointer_s<n and answer_s[pointer_s]!='':
            pointer_s+=1
        
        if pointer_s==n:
            break

        answer_s[pointer_s]=chr(pointer_c+97)
        count2[pointer_c]+=1

    print(answer)
    print(''.join(answer_s))

    
    


