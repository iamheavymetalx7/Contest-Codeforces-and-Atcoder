import sys, threading
import math
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
 
 
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
    
 
'''
Note that the size of the array 
doesn't change parity, since it 
always decreases by 2. Let's count 
the number of distinct elements, 
call it x.

If x is the same parity as n
 (the length of the array), 
 then we can make sure all of 
 these x distinct elements 
 stay in the array by removing 
 two elements at a time.

Otherwise, x isn't the same 
parity as x. Then x-1 is the 
same parity as n, and we can 
make sure x-1 distinct elements stay
 in the array by removing two
  elements at a time. So the 
  answer is x if x and n have 
  the same parity, and x−1 otherwise.
''' 
def solve(t):
    n=int(input())
    A=list(map(int, input().split()))

    c=Counter(A)
    l=len(c)
    n=len(A)

    if l%2==n%2:
        print(l)
    else:
        print(l-1)




 
 
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
    sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        solve(i+1)
 
 
if __name__ == '__main__':
    main()