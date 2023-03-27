list_1 = [int(input("введите число в список: ")) for _ in range(int(input('введите длину списка: ')))]
max_sum = list_1[-2] + list_1[-1] +list_1[0]
sum = 0
for i in range(len(list_1)-1):
    sum = list_1[i - 1] + list_1[i] + list_1[i + 1]
    # print(sum)
    if sum > max_sum:
        max_sum = sum
print(max_sum)

