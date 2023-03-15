# // Problem: B. Little Girl and Game
# // Contest: Codeforces - Codeforces Round 169 (Div. 2)
# // URL: https://codeforces.com/contest/276/problem/B
# // Memory Limit: 256 MB
# // Time Limit: 2000 ms
# // 
# // Powered by CP Editor (https://cpeditor.org)

from collections import Counter
def solve():
	s=input()
	dic=Counter(s)
	cnt=0
	
	for k,v in dic.items():
		if v%2==1:
			cnt+=1
	if cnt<=1:
		print("First")
		return


	if cnt%2:
		print("First")
		return
	else:
		print("Second")
		return
solve()