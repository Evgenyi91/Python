n = int(input('введте чсисло: '))
x = 0
for i in range(n):
    if 2**x <= n:
     x+=1
     print(2**(x-1), end = ' ')

