import sys
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

t=int(input())
for tests in range(t):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    E=[[] for i in range(n)]

    for i in range(n-1):
        x,y=map(int,input().split())
        x-=1
        y-=1
        E[x].append(y)
        E[y].append(x)

    XOR=0
    for a in A:
        XOR^=a

    if XOR==0:
        print("YES")
        continue

    ROOT=0

    

    QUE=[ROOT] 
    Parent=[-1]*(n+1)
    Parent[ROOT]=n # ROOTの親を定めておく.
    TOP_SORT=[] # トポロジカルソート
    Child=[[] for i in range(n)]

    while QUE: # トポロジカルソートと同時に親を見つける
        x=QUE.pop()
        TOP_SORT.append(x)
        for to in E[x]:
            if Parent[to]==-1:
                Parent[to]=x
                Child[x].append(to)
                QUE.append(to)

    ANS=0

    for x in TOP_SORT[::-1]:
        if x==0:
            continue

        sc=A[x]

        for to in Child[x]:
            sc^=A[to]

        if sc==XOR:
            ANS+=1
            A[x]=0
        else:
            A[x]=sc

    #print(ANS)

    if ANS>=2 and k>=3:
        print("YES")
    else:
        print("NO")

        

    


    

    
