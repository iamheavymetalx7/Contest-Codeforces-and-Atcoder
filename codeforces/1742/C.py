t = int(input())
for _ in range(t):
    input()
    l = []
    for i in range(8):
        l.append(input())
    ans = 'B'
    for i in range(8):
        if(l[i] == 8 * 'R'):
            ans = 'R'
        
    
    print(ans)