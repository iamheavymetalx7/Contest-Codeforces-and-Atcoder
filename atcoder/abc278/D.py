##https://atcoder.jp/contests/abc278/tasks/abc278_d
'''
^-------------------- TLE SOLUTION ---------------^
N = int(input())
arr=list(map(int, input().split()))

Q=int(input())

for i in range(Q):
    q_ = list(map(int, input().split()))

    if q_[0]==1:
        arr=[q_[1]]*N
    elif q_[0]==3:
        print(arr[q_[1]-1])
    else:
        arr[q_[1]-1]+=q_[2]
^-------------------- TLE SOLUTION ---------------^
'''

from collections import defaultdict

N = int(input())
arr=list(map(int, input().split()))
dic=defaultdict(int)
Q=int(input())
flag=0
update=0
for i in range(Q):
    q = list(map(int, input().split()))
## Turn on the initialization flag and save the initialization value
    if q[0]==1:
        flag=1
        update=q[1]
        ##Initialize A_Dic
        dic=defaultdict(int)
#Assign query[2] to #A[query[1]-1]
    elif q[0]==2:
        if q[1]-1 in dic:
            dic[q[1]-1]+=q[2]
        else:
            dic[q[1]-1]=q[2]

#prints A[query[1]-1]
    elif q[0]==3:
        if flag:
            ## If initialized, initialized value + amount of change after initialization
            print(update+dic[q[1]-1])
        else:
            ##initial value + amount of change if not initialized
            print(arr[q[1]-1]+dic[q[1]-1])

