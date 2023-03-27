list_1 = [int(input()) for _ in range(int(input('-->')))]
list_2 = [int(input()) for _ in range(int(input('-->')))]
list_1 = set(list_1)
list_2 = set(list_2)
print(*list_1)
print(*list_2)
list_3 = list_1.intersection(list_2)
list_3 = list(list_3)
list_3.sort()
print(*list_3)