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

'''
For simplifications, in the following solution we define lovely integer as an even-length positive palindrome number.

An even-length positive integer is lovely if and only if the first half of its digits is equal to the reverse of the second half.

So if a and b are two different 2k-digit lovely numbers, then the first k digits of a and b differ in at least one position.

So a is smaller than b if and only if the first half of a is smaller than the the first half of b.

Another useful fact: The first half of a a lovely number can be any arbitrary positive integer.

Using the above facts, it's easy to find the first half of the n-th lovely number — it exactly equals to integer n. When we know the first half of a lovely number, we can concatenate it with its reverse to restore the lovely integer. To sum up, the answer can be made by concatenating n and it's reverse together.


'''
    
def solve():
    n=si()
    rev_n=n[::-1]
    new_string = n+rev_n
    number = int(new_string)

    print(number)


    
    
def main():

    solve()
 
if __name__ == '__main__':
    main()
    
 


