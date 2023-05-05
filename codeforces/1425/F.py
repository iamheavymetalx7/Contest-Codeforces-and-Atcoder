import sys
def query(a, b):
    print(f'? {a} {b}')
    sys.stdout.flush()
    return int(input())


n = int(input())

first_three = query(1, 3)

first_two = query(1, 2)
twoand3 = query(2, 3)

third = first_three - first_two
numbers = [first_three - twoand3, first_three - third - (first_three - twoand3), third]
# print(f'{numbers=}')
total = first_three
for i in range(4, n + 1):
    n = query(1, i) - total
    numbers.append(n)
    total += n

print("!", ' '.join(map(str, numbers)))



