from copy import deepcopy

n, s = map(int,input().split())

box = []

for i in range(n):
    tmplist = list(map(int,input().split()))
    box.append(tmplist)      

def jegop(abox,bbox):
    nbox = deepcopy(abox)
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += (abox[i][k])*(bbox[k][j])
            nbox[i][j] = tmp%1000
    return(nbox)

t = 1
while s < 2**t-1 :
    t += 1

box_list=[box]
tmp_box = box

for i in range(t) :
    tmp_box = jegop(tmp_box,tmp_box)
    box_list.append(tmp_box)

tmp_s = s
dab_list = []

for i in range(t) :
    if tmp_s//2 == 1:
        dab_list.append(box_list[i])
    tmp_s = tmp_s//2

dab_list.append(box_list[-1])

ans = dab_list[0]

if len(dab_list) > 1:
    for i in range(1,len(dab_list)):
        ans = jegop(ans,dab_list[i])

print(ans)

# for i in range(n):
#     if i != n:
#         for j in range(n):
#             if j == n :
#                 print(ans[i][j])
#             else :
#                 print(ans[i][j], end=' ')
#         print()
#     else :
#         for j in range(n):
#             if j == n :
#                 print(ans[i][j])
#             else :
#                 print(ans[i][j], end=' ')
# b = 제곱 수 

# b 를 2a 승으로 구함 
# b 2a + 2b + 2c ... 형으로 구함

# b의 
# 1 2 4 8 16 2a 까지 / 리스트를 저장.

# 앞에서 부터 곱해서 최종값 구함. 매 레스트값은 1000의 나머지 처리 

