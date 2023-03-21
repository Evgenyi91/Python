n = abs(int(input('введите длину списка: ')))
A = []
X = int(input('введите искомое число: '))

index = 0
for i in range(n):
    v = int(input('введите число в список: '))
    A.append(v)
min = abs(X - A[0])

for i in range(1, n):
        count = abs(X - A[i])
        if count < min:
            min = count
            index = i
print(f'Число {A[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A[index])}')
