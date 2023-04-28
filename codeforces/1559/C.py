# /**
# * author:Hisoka-TheMagician
# * created: 28/04/2023 11:29 Chennai, India
# **/
        

        # n-1 roads from i to i+1
        # n roads: 0 : i ----> n+1
        #          1 : n+1 -----> i


## we are using 0 based indexing for a[i], where as question uses 1-based indexing
## be careful next time!!
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if not a[-1]:
        print(*range(1, n+2))
    elif a[0]:
        print(n+1, *range(1, n+1))
    else:
        for i in range(n-1):
            if ((not a[i]) and (a[i+1])):
                print(*range(1, i+2), n+1, *range(i+2, n+1))
                break
        else:
            print(-1)