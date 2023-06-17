# /**
# * author:Hisoka-TheMagician
# * created: 17/06/2023 11:04 Chennai, India
# **/
        



## TUTORIAL## HUANGXW's CODE
                                                                                                                        

from __future__ import division, print_function

import os,sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

from bisect import bisect_left as lower_bound, bisect_right as upper_bound 

def lmii():
    return list(map(int,input().split()))

def ii():
    return int(input())

def si():
    return str(input())
def lmsi():
    return list(map(str,input().split()))
def mii():
    return map(int,input().split())

def msi():
    return map(str,input().split())

i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')

import threading
def dmain():
    sys.setrecursionlimit(1000000)
    threading.stack_size(1024000)
    thread = threading.Thread(target=main)
    thread.start()


def joro(L):
    return(''.join(map(str, L)))


def decimalToBinary(n): return bin(n).replace("0b","")


def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

from math import *
def npr(n, r):
    return factorial(n) // factorial(n - r) if n >= r else 0
 
 
def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r)) if n >= r else 0
 
 
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    li = []
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
 
    for p in range(2, len(prime)):
        if prime[p]:
            li.append(p)
    return li
 
 
def primefactors(n):
    factors = []
    while (n % 2 == 0):
        factors.append(2)
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):  # only odd factors left
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:  # incase of prime
        factors.append(n)
    return factors
         
    
def read():
    sys.stdin  = open('input.txt', 'r')  
    sys.stdout = open('output.txt', 'w') 
def tr(n):
    return n*(n+1)//2


        
from collections import Counter, defaultdict, deque

def cnt_diff(x):
    n=str(x)
    return len(set(n))


a=set()

for i in range(1,10):
    for j in range(1,11):
        a.add(int(str(i)*j))

a = sorted(a)


b=set()



def dfs(i,j,s,k):
    if k==11:
        return

    global b

    if s:
        b.add(int(s))
    

    dfs(i,j,s+str(i),k+1)
    dfs(i,j,s+str(j),k+1)


for i in range(10):
    for j in range(10):
        dfs(i,j,"",0)

b= sorted(b)
# print(b)

from bisect import bisect_left, bisect_right
def solve():
    import sys
    input =sys.stdin.buffer.readline

    n,k=mii()

    if k==1:
        val =a[bisect_left(a,n)]
        print(val)
    else:
        val = b[bisect_left(b,n)]
        print(val)








    # n,k=mii()

    # ele = cnt_diff(n)

    # if ele<=k:
    #     print(n)
    #     return

    
    
    # xx= str(n)


    # ans=[]
    # p=len(xx)
    # if k==1:
    #     for i in range(1,10):
    #         ans.append(int(str(i)*(p)))
    #     ans.sort()
    #     for el in ans:
    #         if el>=n:
    #             res=el
    #             break
    #     print(res)
    #     return

    # l,sl,tl = int(xx[0]),int(xx[1]), int(xx[2])

    # ans1 = xx[0]+xx[1]*(len(xx)-1)
    # ans2 = str(int(xx[0]))+ "0"*(len(xx))
    # ans3 = xx[0]+ str(int(xx[1])+1) + xx[0]*(len(xx)-2)
    # ans4 = xx[0]*len(xx)
    # mini=10**9
    # ans =0
    # if int(ans1)>n and abs(n-int(ans1))<mini:
    #     ans = int(ans1)
    #     mini = abs(n-int(ans1))

    # if int(ans2)>n and abs(n-int(ans2))<mini:
    #     ans = int(ans2)
    #     mini = abs(n-int(ans2))


    # if int(ans3)>n and abs(n-int(ans3))<mini:
    #     ans = int(ans3)
    #     mini = abs(n-int(ans3))

    # if int(ans4)>n and abs(n-int(ans4))<mini:
    #     ans = int(ans4)
    #     mini = abs(n-int(ans4))
    
    # print(ans)
    
        
            
            
def main():
    for i in range(ii()):
        solve()
                
            
                
                
                
                
            
    
            
            
    
    
    
    
        
            
    
            
            
            
        
    
        
    
    
        
        
        

            
                    
                
                    
                    
                    
                    
                    
                    
        
                
        
        
       
    
           
          
          
                
            
        
                
    
        
        
        
       
            
                
        




# region fastio
# template taken from https://github.com/cheran-senthil/PyRival/blob/master/templates/template.py

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion


if __name__ == "__main__":
    # read()
    main()
    #dmain()

# Comment Read()