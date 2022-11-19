N, Q = map(int, input().split())
cnt = set()
 
for _ in range(Q):
  T, A, B = map(int, input().split())
  if T == 1:
    cnt.add((A, B))
  if T == 2:
    cnt.discard((A, B))
  if T == 3:
    if (A, B) in cnt and (B, A) in cnt:
      print('Yes')
    else:
      print('No')