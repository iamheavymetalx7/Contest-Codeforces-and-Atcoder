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
 
##      implementation     # #
# # # # # # # # # # # # # # # #

def solve(t):
    n=int(input())
    s = list(input())+["2"]
    a=list(map(int, input().split()))
    to_ret=0
    N_lid=0
    i=0
    while i<n:
        if s[i]=="0" and s[i+1]=="1":
            if a[i]>a[i+1]:
                to_ret+=a[i]
                s[i+1]="0"
                N_lid = a[i+1]
            else:
                N_lid=a[i]
        elif N_lid>a[i] and s[i]=="1":
            to_ret+=N_lid
            s[i]="0"
            N_lid=a[i]
        elif s[i]=="1":
            to_ret+=a[i]
        i+=1
    print(to_ret)


    


 
 
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