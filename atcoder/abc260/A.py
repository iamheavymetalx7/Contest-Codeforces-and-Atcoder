s =input()
from collections import Counter

sc =Counter(s)
for i,j in sc.items():
	if j == 1:
		print(i)
		break
else:
	print(-1)
