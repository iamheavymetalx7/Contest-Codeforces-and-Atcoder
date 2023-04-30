# ﷽
from itertools import accumulate
import sys
input = lambda: sys.stdin.readline().strip()
mod=7+10**9
def inlst():return [int(i) for i in input().split()]

def solve():
    n,q=inlst()
    lst=inlst()
    dp=[0]*n
    for i in range(2,n):
          if lst[i]<=lst[i-1] and lst[i-1]<=lst[i-1-1]:dp[i]=1
    dp=[0]+list(accumulate(dp))
    # print(dp)
    for i in range(q):
          a,b=inlst()

          if a==b:print(1)
          elif a+1==b:print(2)
          else:
                # print(b-a+1,(dp[b]-dp[a]))
                print(b-a+1-(dp[b]-dp[a+1]))



if __name__ == "__main__":
    # for i in range(int(input())):
        solve()
