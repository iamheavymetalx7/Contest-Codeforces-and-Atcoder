import sys, threading
import math
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq

def dfs(node,ans,adj,vis):
    if vis[node]:
        return
    
    for child in adj[node]:
        dfs(child,ans,adj,vis)

        for x in ans[child]:
            ans[node].add(x)
    vis[node]=1
    return


def solve(t):
    n=int(input())
    ar=[]
    for i in range(n):
        ar.append(str(input()))

    adj=defaultdict(list)
    vis=[0]*n
    ans=[{i+1} for i in range(n)]
    for i in range(n):
        for j in range(n):
            if ar[i][j]=="1":
                adj[j].append(i)

    for i in range(0,n):
        dfs(i,ans,adj,vis)

    for an in ans:
        print(len(an),*an)



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




