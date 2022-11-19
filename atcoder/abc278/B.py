h,m = map(int,input().split())
for i in range(24*60+10):
    a = h//10
    b = h%10
    c = m//10
    d = m%10

    if 0 <= a*10+c <= 23 and 0 <= b*10+d <= 59:
        print(h,m)
        exit()
    
    m += 1
    if m == 60:
        m = 0
        h += 1
        h %= 24

