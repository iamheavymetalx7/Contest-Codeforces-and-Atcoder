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
    n = int(input())
    a=[]
    for _ in range(n):
        a.append(list(input()))
    # print(a)
    score= []

    for i in range(n):
        cnt=0
        ss = a[i]
        for j in range(n):
            if ss[j]=="o":
                cnt+=1
        score.append([cnt,i])
    score.sort(key = lambda x:-x[0])

    for x,y in score:
        print(y+1,end=" ")
def main():
    solve()
if __name__ == "__main__":
    main()