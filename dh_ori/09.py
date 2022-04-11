n, s = map(int,input().split())
box = []
for i in range(n):
    tmplist = list(map(int,input().split()))
    box.append(tmplist)      

def jegop(abox,bbox):
    nbox = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += (abox[i][k])*(bbox[k][j]) %1000
            nbox[i].append(tmp)
    return nbox

def ans(b) :
    if b == 1 :
        return box
    #### last 수정 제곱을 매번하지 않고 수를 미리 구해둠
    ### 계속 틀린 이유! 미리 계산이 자주되는 결과값 두개를 미리 저장

    half = ans(b//2)
    squarehalf = jegop(half, half)

    if b%2 ==0:
        return squarehalf
    else :
        return jegop(squarehalf,box)



for i in ans(s) :
    for j in i:
        print(j % 1000, end=" ")
    print()

# for i in range(n) :
#     for j in range(n):
#         print(result[i][j], end=' ')
#     print()

# b = 제곱 수 

# b 를 2a 승으로 구함 
# b 2a + 2b + 2c ... 형으로 구함

# b의 
# 1 2 4 8 16 2a 까지 / 리스트를 저장.

# 앞에서 부터 곱해서 최종값 구함. 매 레스트값은 1000의 나머지 처리 

