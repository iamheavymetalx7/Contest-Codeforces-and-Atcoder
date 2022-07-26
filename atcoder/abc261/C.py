n = int(input())
A = [(str(input())) for x in range(n)]

dictionary= {}
 
for i in range(n):
    if A[i] in dictionary:
        print("{}({})".format(A[i],dictionary[A[i]]))
        dictionary[A[i]] += 1
    else:
        print(A[i])
        dictionary[A[i]] = 1