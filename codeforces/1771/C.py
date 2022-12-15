from collections import Counter
from math import gcd
def linar_seive(n):
    is_composite=[False for i in range(n+1)]
    primes=[]
    for i in range(2,n+1):
        if not is_composite[i]:
            primes+=[i]
        j=0
        while j<len(primes) and i*primes[j]<=n:
            is_composite[i*primes[j]]=True
            if i%primes[j]==0:
                break
            j+=1
    return primes

def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3
 
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + 1) % n
                f = gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + 1) % n, (y * y + 1) % n
                    y = (y * y + 1) % n
                    f = gcd(abs(x - y), n)
                if f != n:
                    return f
    return n
 
 

def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)
t=int(input())

def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    check=set()
    for number in arr:
        for num in prime_factors(number):
            if num in check:
                print('YES')
                return
            check.add(num)
        
    print('NO')

while t:
    solve()
    t-=1