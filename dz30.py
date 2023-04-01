list_1 = []

k = int(input("начало: "))
l = int(input('шаг: '))
j = int(input('количество элементов: '))
p = k + (j-1) * l

for i in range(p+1):
    list_1.append(i)

print(list_1[k::l])
