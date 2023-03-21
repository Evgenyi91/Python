n = int(input('-->'))
list_n = []
k = 3
count = 0 
for i in range(n):
    v = int(input('-->'))
    list_n.append(v)
    

    if k == list_n[i]:
        count+=1
print(count)

   


