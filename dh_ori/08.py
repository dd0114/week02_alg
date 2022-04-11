a, b, c = map(int,input().split())
t = 0
m_list = []

while b > 2**t :
    t += 1

m =b
n =0

for i in range(t-1) :
    m = m // 2
    n = m % 2
    m_list.append(n)    

m_list.append(1)

na = a%c
na_list = [a%c] 

for i in range(t-1):
    na = (na**2)%c
    na_list.append(na)

ans = 1

for i in range(t):
    if m_list[i] == 1:
        ans = ans * na_list[t-1-i]

print (ans%c)

# 목(a) + 나머지A
# 목(ㅁ) + 나머지 끼리 곱해서 나머지와 같다,

# b를 2**n +2**(n-1) + 꼴로 나타냄
# 리스트에서 끌고 옴  (나머지1 * 나머지2 * 나머지3 ~~) /c 로값을 구함


# 전체 나머지 리스트를 반으로 나눈다. 앞뒤 리스트를 비교 틀리면 false. 다맞으면 리스트를 반환
#  나머지리스트 [b % (len나머지는 나머지리스트)]