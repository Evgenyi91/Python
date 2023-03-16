n = int(input('введте чсисло: '))
n_list = []

for i in range(n):
    m = int(input('введте 0 или 1: '))
    n_list.append(m)

m_zero = 0
m_one = 0
for i in n_list:
    if i == 0:
        m_zero +=1
    elif i == 1:
        m_one += 1

print(m_one if m_one < m_zero else m_zero)



