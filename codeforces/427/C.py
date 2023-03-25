## strongly connected components!!
# SCC - Kosaraju's Algo
# By aayush_chhabra, contest: Codeforces Round 244 (Div. 2), problem: (C) Checkposts, Accepted, #, Copy
from  collections import defaultdict,Counter
from sys import setrecursionlimit,stdin
setrecursionlimit(10**5)
import threading
input=stdin.readline

def dfs(node,vis,g,ans):
    vis.add(node)
    for i in g[node]:
        if i not in vis:
            dfs(i,vis,g,ans)
    ans.append(node)
    return

def main():
    n=int(input())
    g=defaultdict(list)
    graph_reversed=defaultdict(list)

    lst=list(map(int,input().split()))

    for i in range(int(input())):
        x,y=map(int,input().split())
        g[x].append(y)
        graph_reversed[y].append(x)
        
    vis=set()
    order=[]
    cost=0
    for ind in range(1,n+1):
        if ind not in vis:
            dfs(ind,vis,g,order)
    order=order[::-1]

    vis=set()
    ans=0
    total=1
    # component=[]
    for ind in order:
        if ind not in vis:
            component=[]
            dfs(ind,vis,graph_reversed,component)
            ls=[lst[i-1] for i in component]
            cnt=Counter(ls)
            mn=min(cnt.keys())
            ans+=mn
            total=(total*cnt[mn])%(10**9+7)
    print(ans,total)
threading.stack_size(10 ** 8)
t = threading.Thread(target=main)
t.start()
t.join()