for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    f = [0]*26
    g = [0]*26
    for x in s:
        if 'a' <= x <= 'z':
            f[ord(x) - ord('a')] += 1
        else:
            g[ord(x) - ord('A')] += 1
    
    ans = 0
    for i in range(26):
        x = min(f[i], g[i])
        ans += x
        f[i] -= x
        g[i] -= x
        mx = max(f[i], g[i])
        if mx > 1:
            ans += min(k, mx//2)
 
        k -= min(k, mx//2)
 
    print(ans)