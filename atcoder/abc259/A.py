N,M,X,T,D = map(int, input().split())

initial_height = T-D*X

if M>X:
  print(T)
elif M==0:
  print(initial_height)
else:
  print(initial_height+D*M)

