import sys, threading
import math
import time
from os import path
from collections import defaultdict, Counter, deque, OrderedDict
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
 
 
# # # # # # # # # # # # # # # #
#       JAI SHREE RAM         #
# # # # # # # # # # # # # # # #
 
 
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
##for sure this was greedy.
# the main observation was to see that we do
#  not have a_u<=a_v<=a_w for pairwise distinct
# vertices u,v and w.


# Creates a sorted dictionary (sorted by key)

'''

from collections import OrderedDict

dict = {'ravi': '10', 'rajnish': '9',
		'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)

OrderedDict preserves the order 
in which the keys are inserted. 
A regular dict doesn’t track the 
insertion order and iterating it 
gives the values in an arbitrary order. 

'''


def solve(t):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()

    if a[0]==a[-1]: #all elets are same
        return n//2
    dic = OrderedDict()
    for i in range(n):
        dic[a[i]]=dic.get(a[i],0)+1

    sum1=0
    maxi=0
    for i in dic.keys():
        sum1+=dic[i]
        maxi=max(maxi,sum1*(n-sum1))

    return maxi
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        z = solve(i+1)
        print(z)
 
if __name__ == '__main__':
    main()