n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
ans = []
A = []
B = []
C = []
for i in range(n):
    A.append([a[i], -i])
A.sort(reverse = True)
 
for i in range(x):
    ans.append(A[i][1] *(-1))

for i in range(n):
    if i not in ans:
        B.append([b[i], -i])
B.sort(reverse = True)


for i in range(y):
    ans.append(B[i][1] *(-1))
for i in range(n):
    if i not in ans:
        C.append([a[i]+b[i], -i])
C.sort(reverse = True)
for i in range(z):
    ans.append(C[i][1] *(-1))
ans.sort()
for i in ans:
    print(i+1)