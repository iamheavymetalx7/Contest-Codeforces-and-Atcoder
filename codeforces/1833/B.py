# # /**
# # * author:Hisoka-TheMagician
# # * created: 19/05/2023 20:10 Chennai, India
# # **/
        




# #bisect.bisect_left(a, x, lo=0, hi=len(a)) is the analog of std::lower_bound()
# #bisect.bisect_right(a, x, lo=0, hi=len(a)) is the analog of std::upper_bound()
# #from heapq import heappop,heappush,heapify #heappop(hq), heapify(list)
# #from collections import deque as dq #deque  e.g. myqueue=dq(list)
# #append/appendleft/appendright/pop/popleft
# #from bisect import bisect as bis #a=[1,3,4,6,7,8] #bis(a,5)-->3
# #import bisect #bisect.bisect_left(a,4)-->2 #bisect.bisect(a,4)-->3
# #import statistics as stat  # stat.median(a), mode, mean
# #from itertools import permutations(p,r)#combinations(p,r)
# #combinations(p,r) gives r-length tuples #combinations_with_replacement
# #every element can be repeated
        
# #Note direct assignment to check somethings doesnt work always
# #say there exists s (list) then ss=s and if we edit ss, it edits s as well
# #always try to use ss=s.copy() if u wish to make changes to ss and not reflect them in s.
# #For example: see **1379A - Acacius and String** for reference
    
# import sys, threading, os, io 
# import math
# import time
# from os import path
# from collections import defaultdict, Counter, deque
# from bisect import *
# from string import ascii_lowercase
# from functools import cmp_to_key
# import heapq
# from bisect import bisect_left as lower_bound
# from bisect import bisect_right as upper_bound
# from io import BytesIO, IOBase								
# # # # # # # # # # # # # # # # #
# #       JAI SHREE RAM         #
# # # # # # # # # # # # # # # # #
 
 
# def lcm(a, b):
#     return (a*b)//(math.gcd(a,b))
 
 
# input = lambda: sys.stdin.readline().rstrip()
# def lmii():
#     return list(map(int,input().split()))

# def ii():
#     return int(input())

# def si():
#     return str(input())
# def lmsi():
#     return list(map(str,input().split()))
# def mii():
#     return map(int,input().split())

# def msi():
#     return map(str,input().split())

# i2c = lambda n: chr(ord('a') + n)
# c2i = lambda c: ord(c) - ord('a')
    
    
# # if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
# #     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
# #     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
# # else:
# #     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    
# def solve():
#     n,k=mii()

#     a=lmii()
#     b=lmii()
#     asort=sorted(a)
#     bsort=sorted(b)

#     # print(asort)
#     # print(bsort)

#     dic=defaultdict(deque)

#     for i,ele in enumerate(asort):
#         dic[ele].append(i)
    
#     # print(dic)

#     newb=[0]*(n)

#     for i,ele in enumerate(a):
#         idx = dic[ele].popleft()
#         newb[i] = bsort[idx]
    
#     print(*newb)
#     # a=lmii()


#     # dicaa=defaultdict(list)

#     # for i,ele in enumerate(asort):
#     #     dicaa[ele].append(i)
    
    

#     # b=lmii()

#     # b.sort()
#     # asort=sorted(a)

#     # print(asort)
#     # print(b)


#     # dica=defaultdict(list)

#     # for i,ele in enumerate(asort):
#     #     dica[ele].append(i)
    
#     # print(dica)

#     # dicb = defaultdict(int)

#     # for i,ele in enumerate(b):
#     #     dicb[i] = (ele)
    
#     # print(dicb)

#     # newb=[0]*n
#     # seen=set()
#     # for k,v in dicaa:
#     #     seen.add(ele)
#     #     if ele not in seen:
#     #         for idx in dica[ele]:
#     #             print(idx)
#     #             newb[i]=dicb[idx]
#     #             break
    
#     # print(newb)











    
    
    
    
# xxx=ii()
# for _ in range(xxx):
#     solve()

# /**
# * author:Hisoka-TheMagician
# * created: 20/05/2023 08:33 Chennai, India
# **/
        




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
        
#Note direct assignment to check somethings doesnt work always
#say there exists s (list) then ss=s and if we edit ss, it edits s as well
#always try to use ss=s.copy() if u wish to make changes to ss and not reflect them in s.
#For example: see **1379A - Acacius and String** for reference
    
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
 
 
input = lambda: sys.stdin.readline().rstrip()
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
    
    
def solve():
    n,k=mii()
    a=lmii()
    b=lmii()

    c = sorted([(a[i],i) for i in range(n)])
    
    d= sorted([(b[i],i) for i in range(n)])

    ans=[0]*n
    for i in range(n):
        ans[c[i][1]]=d[i][0]
    
    print(*ans)
    
    
    
xxx=ii()
for _ in range(xxx):
    solve()