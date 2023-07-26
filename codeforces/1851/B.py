from bisect import *
from heapq import *
from collections import defaultdict,Counter
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")


for _ in range(int(input())):
    n = int(input())
    a=list(map(int, input().split()))

    b=sorted(a)

    for i in range(n):
        if a[i]%2!=b[i]%2:
            print("NO")
            break
    else:
        print("YES")