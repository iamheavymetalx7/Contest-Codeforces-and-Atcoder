from bisect import *
from heapq import *
from collections import defaultdict,Counter
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")





def solve():
    s=  input()
    n = len(s)
    for i in range(1,n,2):
        if s[i]!="0":
            print("No")
            return
        
    print("Yes")

def main():
    solve()
if __name__ == "__main__":
    main()