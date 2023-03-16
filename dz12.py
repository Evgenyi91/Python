s = int(input('введте чсисло: '))
p = int(input('введте чсисло: '))

for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(x, y)