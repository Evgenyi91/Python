list_1 = [int(input("введите число в список: ")) for _ in range(int(input('введите длину списка: ')))]

k = int(input("диапазон от: "))
l = int(input('диапазон до: '))
print(list_1)

for i in list_1:
    if i >= k and i <= l:
        # list_2.append(i)

        print( f"[{list_1.index(i)}]", end = ' ') 
