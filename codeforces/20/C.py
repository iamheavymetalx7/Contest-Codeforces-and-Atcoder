from heapq import *
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for i in range(n + 1)]
for i in range(m):
	x, y, w = map(int, input().split())
	if x!=y:
		g[x].append((y, w))
		g[y].append((x, w))
path = [i for i in range(n + 1)]
dis = [10**12] * (n + 1)
hp = [(0, 1)]
while hp:
	dcur, cur = heappop(hp)
	for v, w in g[cur]:
		if dcur + w < dis[v]:
			dis[v] = dcur + w
			path[v] = cur
			heappush(hp, (dis[v], v))
l = [n]
x = n
if dis[n] != 10**12:
	while x != 1:
		x = path[x]
		l.append(x)
	print(*l[::-1])
else:print(-1)