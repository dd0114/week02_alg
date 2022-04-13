import copy
n = int(input())

# 리스트 받음
t_list = list(map(int,input().split()))

m_list = [[t_list[0],0]]
m = len(m_list)
dab_list = [0]*n

for i in range(1,n) :
    while len(m_list) != 0:
        pop_m = copy.deepcopy(m_list.pop())
        if t_list[i] < pop_m[0] :
            dab_list[i] = pop_m[1]+1
            m_list.append(pop_m)
            m_list.append([t_list[i],i])
            break

    if len(m_list) == 0:
        dab_list[i]=0
        m_list.append([t_list[i],i])

print(*dab_list)




# 앞에서부터 맥스리스트랑 비교
# 맥스리스트 (6,0)
# 답리스트 0
# 
# 인덱스와 맥스리스트에 앞에서 부터 비교. 
# 뒤에서 부터 비교한다. (팝해서) 
#   리스트가 높이가 크면 다음 인덱스와 비교
#   높이가 작으면 (인덱스 값 복사) -> 팝한거 원위치 + 맥스리스트에 저장
#   다 돌 았는데 없으면?(맥스리스트가 비워지면) -> 본인이 맥스 리스트 0

# 답리스트를 출력

