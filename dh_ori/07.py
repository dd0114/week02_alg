N = int(input())

N_box = []

for i in range(N):
    N_box.append(list(map(int,input().split())))

one_count = 0
zero_count = 0

def oneorzero(n,x,y):
    if n == 1:
        return (N_box[y][x]+1)

    else :            
        for i in range(n-1) :
            if N_box[y][x] != N_box[y][x+i]:
                return False
        
        for i in range(n-1) :
            if N_box[y] != N_box[y+1]:
                return False
        
        return(N_box[y][x]+1)

def box(n,x,y) : 
    global one_count
    global zero_count
    result = oneorzero(n,x,y) 
    if- result == False :
        box ((n//2),x,y)
        box ((n//2),x+(n//2),y)
        box ((n//2),x,y+(n//2)) 
        box ((n//2),x+(n//2),y+(n//2))

    elif result == 2 :
        one_count += 1

    else : #result == 0 :
        zero_count += 1

box(N, 0, 0)
print(zero_count)
print(one_count)

# 함수는 (길이와 시작 좌표)
# 스캔을 한다. (한행이 모두 같고 행고 다른 열이 같으면) 
# 시작, ~ 시작 + 길이-1 만큼 
# 시작부터 길이

# 카운트를 올린다.

# 안니면 4등분을한다. 길이 = n/2 좌표는 기존과 동일 / 기존 +n/2 씩 
#  각 첫좌표부터 함수를 실행
