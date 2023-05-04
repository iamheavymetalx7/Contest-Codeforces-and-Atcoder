# 
#  author:Hisoka-TheMagician
# 
# 
# 2023-05-04 14:41:45$
# Problem: B. Absent Remainder
# Contest: Codeforces - Educational Codeforces Round 118 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1613/B
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# 
from math import *
def solve():
	n=int(input())
	
	to_get = n//2
	k=0
	
	a=list(map(int, input().split()))
	
	mini= min(a)
	
	for i in range(n):
		
		if a[i]!=mini:
			print(a[i],mini)
			k+=1
		if k==to_get:
			break
	
	# print('_'*10)
	
	

	
xx=int(input())
for _ in range(xx):
	solve()