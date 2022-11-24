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

def solve(t):
    n,q=map(int,input().split())
    N = list(map(int,input().split()))
    even,odd = 0,0

    for i in range(n):
        if N[i]%2==0:
            even+=1
        else:
            odd+=1

    total=sum(N)
    for i in range(q):
        type,x=map(int, input().split())
        if type==1:
            total+=odd*x
            if x%2:
                even=n 
                odd=0
        elif type==0:
            total+=even*x
            if x%2:
                odd=n
                even=0     
        print(total)   
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