n = input('введите шестизначное число: ')
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])
e = int(n[4])
f = int(n[5])


if len(n) != 6:
    print('не корректное число, перезапустите программу и введите шесть цифр без пробела')
elif  a + b + c == d + e + f:
    print('yes')
else:
    print('no') 