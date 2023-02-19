import sys, threading
import math
import time
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
 
 
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
    n,m=mii()
    a=lmii()
    b=lmii()

    summ=0
    for ele in b:
        summ+=a[ele-1]
    
    print(summ)
    
    
def main():
    # if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/input.txt"):
    #     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/input.txt", 'r')
    #     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/output.txt", 'w')
    #     start_time = time.time()
    #     print("--- %s seconds ---" % (time.time() - start_time))
 
 
    # sys.setrecursionlimit(10**5)
 
 
    solve()
 
 
if __name__ == '__main__':
    main()
    
 



#print(" ".join(str(i) for i in ans))
#print(" ".join(map(str,ans))) #seems faster
##s=[2, 3, 1, 4, 5, 3]
##sorted(range(len(s)), key=lambda k: s[k])
##gives sorted indices [2, 0, 1, 5, 3, 4]
##m= [[3, 4, 6], [2, 4, 8], [2, 3, 4], [1, 2, 3], [7, 6, 7], [1, 8, 2]]
##m.sort(reverse=True,key=lambda k:k[2]) #sorts m according to 3rd elements
#import bisect  #li = [1, 3, 4, 4, 4, 6, 7]#sorted li, use b search, so log(n)
#bisect.bisect(li,4)-->5 #bisect.bisect_left(li,4)-->2
##def chkprime(n):
##  # assert 1 <= n and n <= 1<<64 # = 18446744073709551616
##  if n == 1: return False
##  if n == 2: return True
##  if n & 1 == 0: return False  
##  if n in st: return True
##  d = (n - 1) >> 1
##  while d & 1 == 0:
##    d >>= 1
##  for a in st:
##    t = d
##    y = pow(a, t, n)
##    while t != n - 1 and y != 1 and y != n - 1:
##      y = (y * y) % n
##      t <<= 1
##    if y != n - 1 and t & 1 == 0:
##      return False
##  return True
############### basic prime testing
##def chkprime(x):
##    if x==2 or x==3:return True
##    if x%2==0 or x<2:return False
##    for i in range(3,int(x**0.5)+1,2):
##        if x%i==0:return False
##    return True
########## pre-compute primes
##pp=[]
##for i in range(2,32*10**3): #3.2*10**4 squares to 10**9
##    if chkprime(i):pp.append(i)
############### prime factoring functions (without pp)
##def pfactors(n):
##    f=[];d=3
##    while n%2==0:f.append(2);n//=2
##    while d*d<=n:
##        while n%d==0:f.append(d);n//=d
##        d+=2
##    if n>1:f.append(n)
##    return f
########################## using pre-computed primes in pp
##def pfactors(n):
##    f=[]
##    if chkprime(n):return [n]
##    for d in pp:
##        #if chkprime(n):break
##        if d*d>n:break
##        if n%d==0:f.append(d);n//=d
##        while n%d==0:n//=d
##    if n>1:f.append(n)
##    return f
####################################################
########pp[n] stores a prime factor of n, using a sieve
##nmx=10**7+1
##pp=[0]*(nmx+1)
##def fill_pp(n):
##    p=2
##    while p*p<n:
##        if not pp[p]:
##            pp[p]=p
##            for i in range(p*p,n,p): #p*p, as we don't need the largest p
##                if not pp[i]:pp[i]=p
##        p+=1
##fill_pp(nmx)
##for i in range(nmx):
##    if not pp[i]:pp[i]=i
###########################################
##### take care that it begins with [1,1,2,...]
##def get_largest_prime_factors(num):
##    # get largest prime factor for each number, using a sieve
##    largest_prime_factors = [1] * num
##    for i in range(2, num):
##        if largest_prime_factors[i] > 1:  # i is not prime
##            continue
##        for j in range(i, num, i): # i is prime prime.append(i)
##            largest_prime_factors[j] = i
##    return largest_prime_factors
##########################################
##def get_smallest_prime_factors(num):
##    # get smallest prime factor for each number, using a sieve, quicker
##    smallest_prime_factors = [1] * num
##    for i in range(2, num):
##        if smallest_prime_factors[i] > 1:  # i is not prime
##            continue
##        smallest_prime_factors[i]=i
##        for j in range(i*i, num, i): # i is prime prime.append(i)
##            smallest_prime_factors[j] = i
##    return smallest_prime_factors
########################################## Pollard Rho algorithm
##from math import gcd
##def pollard_rho(n):
##    """returns a random factor of n"""
##    if n & 1 == 0:return 2
##    if n % 3 == 0:return 3
##    s = ((n - 1) & (1 - n)).bit_length() - 1
##    d = n >> s
##    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
##        p = pow(a, d, n)
##        if p == 1 or p == n - 1 or a % n == 0:continue
##        for _ in range(s):
##            prev = p
##            p = (p * p) % n
##            if p == 1:return math.gcd(prev - 1, n)
##            if p == n - 1:break
##        else:
##            for i in range(2, n):
##                x, y = i, (i * i + 1) % n
##                f = gcd(abs(x - y), n)
##                while f == 1:
##                    x, y = (x * x + 1) % n, (y * y + 1) % n
##                    y = (y * y + 1) % n
##                    f = math.gcd(abs(x - y), n)
##                if f != n:return f
##    return n
##########################################
########## set of 3 functions below uses Pollard Rho to factorize
##def isprime(n):
##    if n <= 1:return False
##    if n == 2:return True
##    if n % 2 == 0:return False
##    A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
##    s = 0
##    d = n - 1
##    while d % 2 == 0:
##        s += 1
##        d >>= 1
##    for a in A:
##        if a % n == 0:
##            return True
##        x = pow(a, d, n)
##        if x != 1:
##            for t in range(s):
##                if x == n - 1:break
##                x = x * x % n
##            else:
##                return False
##    return True
##        
##def pollard(n):
##    if n % 2 == 0:
##        return 2
##    if isprime(n):
##        return n
##    f = lambda x:(x * x + 1) % n
##    step = 0
##    while 1:
##        step += 1
##        x = step
##        y = f(x)
##        while 1:
##            p = gcd(y - x + n, n)
##            if p == 0 or p == n:
##                break
##            if p != 1:
##                return p
##            x = f(x)
##            y = f(f(y))
                    
##def primefact(n):
##    if n == 1:
##        return []
##    p = pollard(n)
##    if p == n:
##        return [p]
##    left = primefact(p)
##    right = primefact(n // p)
##    left += right
##    return sorted(left)