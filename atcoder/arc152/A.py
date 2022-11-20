import sys
import math

N, L = map(int, input().split())
A = list(map(int, input().split()))

# In most of the programming languages 
# (C/C++, Java, etc), the use
#  of else statement has been 
# restricted with the if 
# conditional statements. 
# But Python also allows us
#  to use the else condition 
# with for loops.

# The else block just 
# after for/while is executed 
# only when the loop is 
# NOT terminated by a break statement.


remaining = L

for i in range(N):
    if remaining > A[i]:
        remaining -= (A[i]+1)
    elif remaining == A[i]:
        remaining -= A[i]
    else:
        break
else:
    print('Yes')
    exit()

if A[i:].count(2) > 0:
    print('No')
else:
    print('Yes')
