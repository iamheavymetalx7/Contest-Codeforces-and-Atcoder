## it is a easy recursion problem, if you carefully notice

n,X,Y = map(int, input().split())
def convert_red(n):
  if n<=1:
    return 0
  else: return (convert_red(n-1)+X*convert_blue(n))

def convert_blue(n):
  if n<=1:
    return 1
  else: 
    return (convert_red(n-1)+Y*convert_blue(n-1))

print(convert_red(n))