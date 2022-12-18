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
    
    
def solve(t):
    a,b=mii()
    c,d=mii()
    matrix =[[a,b],[c,d]]
    flag=1
    for i in range(4):
        if (matrix[0][0]<matrix[1][0] and matrix[0][0]<matrix[0][1] and matrix[0][1]>matrix[0][0] and matrix[0][1]<matrix[1][1] and matrix[1][0]<matrix[1][1]):
            flag=0
            break
        zerozro=matrix[0][0]
        matrix[0][0]=matrix[1][0]    
        matrix[1][0]    = matrix[1][1]
        matrix[1][1] = matrix[0][1]
        matrix[0][1] = zerozro

    if flag==0:
        print("YES")
    else:
        print("NO")
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