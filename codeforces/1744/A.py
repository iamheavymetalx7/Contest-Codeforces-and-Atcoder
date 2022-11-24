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
    n=int(input())
    arr=list(map(int, input().split()))
    strng=str(input())
    string = list(strng)
    dic=defaultdict(str)
    for i in range(len(arr)):
        if arr[i] in dic:
            continue
        dic[arr[i]]=string[i]
    A=[]
    for i in range(len(arr)):
        A.append(dic[arr[i]])
    if A==string:
        return "YES"
    return "NO"
 
 
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
    sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        z= solve(i+1)
        print(z)
 
if __name__ == '__main__':
    main()