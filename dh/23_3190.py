from collections import deque

n = int(input())
k = int(input())

apple = []
move = []
snake = deque([[1,1]])
time = 0
dir = 0

for i in range(k):
    apple.append(list(map(int, input().split())))

l = int(input())

for i in range(l):
    move.append(input().split())

for i in range(len(move)):
    now = move[i]
    can = int(now[0]) - time
    for j in range(can):
        time += 1
        if dir%4 == 0 :
            a = [snake[-1][0],snake[-1][1]+1]
        elif dir%4 == 1:
            a = [snake[-1][0]-1,snake[-1][1]]
        elif dir%4 == 2:
            a = [snake[-1][0],snake[-1][1]-1]
        else : #dir%4 =3 :
            a = [snake[-1][0]+1,snake[-1][1]]
        
        if a in snake or 0 in a or n+1 in a:
            print(time)
            exit()
        
        snake.append(a)

        if not a in apple:
            snake.popleft()
        else :
            apple.remove(a)
    if now[1] == 'L':
        dir = (dir+1+4)%4
    elif now[1] == 'D':
        dir = (dir-1+4)%4

while True :
    time += 1
    if dir%4 == 0 :
        a = [snake[-1][0],snake[-1][1]+1]
    elif dir%4 == 1:
        a = [snake[-1][0]-1,snake[-1][1]]
    elif dir%4 == 2:
        a = [snake[-1][0],snake[-1][1]-1]
    else : #dir%4 =3 :
        a = [snake[-1][0]+1,snake[-1][1]]
    
    if a in snake or 0 in a or n in a:
        print(time)
        exit()
    
    snake.append(a)

    if not a in apple:
        snake.popleft()

# 뱀 이동 함수
# 좌표 하나 넣고 하나 팝
# 넣는 방식 - 이동리스트에서 앞에 있는 거 꺼내 옴. 수만큼 이동.

# 타임 +1
# 넣는 좌표가 자신에게 있거나 벽에 닿으면 브레이크
# 넣는 좌표가 사과 리스트에 있으면 팝 무시

# 이동중에 사과 만나면 팝 무시. 
# 이동 끝나면 리스[1] 로 방향 변환

# (현재 방향 설정)

# 방향이 
# 우 / 열 좌표를 증가
# 좌 / 열 좌표 감소
# 상 / 행 좌표 감소
# 하 / 행 좌표 증가 

# 방향 우측 +1 좌측 -1
# 방향 0 우
# 방향 1 상
# 방향 2 좌
# 방향 3 하