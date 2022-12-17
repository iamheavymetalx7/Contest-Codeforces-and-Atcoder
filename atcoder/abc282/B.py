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
    
    
def solve():
    N, M = map(int, input().split())
    arr = []
    all = int('1'*M, 2)
    cnt = 0

    for _ in range(N):
        string = ''
        for s in input():
            if s == 'o':
                string += '1'
            else:
                string += '0'
        arr.append(int(string, 2))
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] | arr[j] == all:
                cnt += 1

    print(cnt)



    
    
def main():
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/output.txt", 'w')
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
 
    solve()
 
 
if __name__ == '__main__':
    main()