n, m = map(int, input().split())
 
Max = n - (m-1)
Max = (Max*(Max-1))//2
 
x = n//m
Min = ((x*(x-1))//2)*m
 
Min += (n%m)*x
 
print(Min, end=" ")
print(Max)