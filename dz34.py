def rifma(puh):
    puh = puh.split()
    puh_1 = []
    for item in puh:
        sum = 0
        for i in item:
            if i in "йуеаыоэюия":
                sum +=1
        puh_1.append(sum)
    return len(puh_1) == puh_1.count(puh_1[0])

puh_2 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rifma(puh_2):
    print('Парам пам-пам')
else:
    print('Пам парам')