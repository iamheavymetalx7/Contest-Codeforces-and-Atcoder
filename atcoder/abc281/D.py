#atcoder Assemble
#upsolving
import sys, threading
import math
import time
from os import path
 
 
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
    N,K,D=mii()
    arr=lmii()
    
    dp = [[[-1] * 106 for _ in range(106)] for _ in range(106)]



    def rec(i,rem,taken):
        if taken == K:
            return 0 if rem==0 else -math.inf
        if i==N:
            return -math.inf

        if dp[i][rem][taken] != -1:
            return dp[i][rem][taken]
        ans =max(rec(i+1,rem,taken), rec(i+1,(rem+arr[i])%D,taken+1)+int((rem+arr[i])/D))
        dp[i][rem][taken]=ans
        return dp[i][rem][taken]

    p=rec(0,0,0,)
    if p<0:
        return -1
    else:
        return int(p*D)

    
    
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/output.txt", 'w')
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
 
    z=solve()
    print(z)
 
if __name__ == '__main__':
    main()