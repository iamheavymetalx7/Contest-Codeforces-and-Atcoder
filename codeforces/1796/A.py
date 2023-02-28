
string=""
for i in range(1,10**5+1):
    if i%3==0:
        string+="F"
    if i%5==0:
        string+="B" 

for _ in range(int(input())):
    m=int(input())
    s=str(input())

    if s in string:
        print("YES")
    else:
        print("NO")
    
 

