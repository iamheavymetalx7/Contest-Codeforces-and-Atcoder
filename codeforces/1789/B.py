for _ in range(int(input())):
    n = int(input())
    s = input()
    ct = 0; c = 0
    for i in range(n//2):
        if s[i] != s[-i-1]:
            if not c: ct += 1; c = 1
        else:
            c = 0
 
    print('Yes' if ct <= 1 else 'No')