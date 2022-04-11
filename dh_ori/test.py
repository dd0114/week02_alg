a, b, c = map(int,input().split())
t = 0
m_list = []

while b > 2**t :
    t += 1

na = a%c
na_list = [a%c] 

for i in range(t):
    na = (na**2)%c
    na_list.append(na)

print(na_list)