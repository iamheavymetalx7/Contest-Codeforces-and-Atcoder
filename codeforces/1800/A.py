for _ in range(int(input())):
    n = int(input())
    s = input().lower()
    l = '#'
    for x in s:
        if x != l[-1]:
            l += x
 
    if l == '#meow':
        print("YES")
    else:
        print('NO') 