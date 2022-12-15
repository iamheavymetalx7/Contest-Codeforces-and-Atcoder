import sys
input=sys.stdin.readline
from math import gcd
Prime = [0] * 10000000
for i in range(3, 10000000, 2) :
    if Prime[i] == 0 :
        j = 3 ; Prime[i] = i
        while i*j <= 10000000 :
            if not Prime[i*j] : Prime[i*j] = i
            j += 2
 
for _ in range(int(input())) :
    a, b = map(int,input().split())
    if gcd(a, b) > 1 : print(0)
    elif b - a == 1 : print(-1)
    elif (b-a)%2 == 0 : print(1)
    else :
        Ans = int(1e7) ; c = b - a
        while c > 1 :
            d = Prime[c]
            Ans = min(Ans, d - a%d)
            c //= d
        
        print(Ans)