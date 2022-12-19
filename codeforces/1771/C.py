from collections import Counter
from math import gcd


def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    # for a in [2, 3, 5, 7]:
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


@memodict
def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    L = []
    for i in range(n-1):
        if arr[i] == arr[i+1] and arr[i] != 1:
            return "YES"
    s = set()
    for a in arr:
        if a != 1:
            for p in prime_factors(a):
                if p in s:
                    return "YES"
                s.add(p)
    return "NO"



import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for i in range(t):
    print(solve())
