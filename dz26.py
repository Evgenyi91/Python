def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    else:
        return a
c = int(input('a-->: '))
d = int(input('b-->: '))
 
print(sum(c, d))