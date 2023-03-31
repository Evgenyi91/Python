def degree_numb(a,b):
        
    if b == 0:
        return 1
    
    
    return  a * degree_numb(a, b-1)
        
c = int(input('a-->: '))
d = int(input('b-->: '))

print(degree_numb(c,d))