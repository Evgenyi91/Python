n = int(input('введите число n: '))
m = int(input('введите число m: '))
k = int(input('введите число m: '))

if k < m *n and ((k % n == 0) or (k % m == 0)):
       print('YES')
else:
       print('NO')