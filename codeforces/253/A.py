with open("input.txt", "r") as fp:
    n, m = map(int, fp.readline().split())
    out = open("output.txt", "w")
    if n>m:
        mini=min(m,n)
        n-=mini
        m-=mini

        ans ="BG"*mini
        ans+="B"*n
        ans+="G"*m
    else:
        mini=min(n,m)
        n-=mini
        m-=mini
        ans="GB"*mini
        ans+="B"*n
        ans+="G"*m

    out.write(ans)
    out.close()