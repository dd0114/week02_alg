# 23. 뱀
import sys
from collections import deque
from copy import deepcopy

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apples = []

for _ in range(K):  
    apples.append(list(map(int, sys.stdin.readline().strip().split())))

L = int(sys.stdin.readline())
changes = deque() # 뱀 방향 변환 정보는 큐에 저장

for _ in range(L):
    changes.append(sys.stdin.readline().strip().split())

snake = deque([[1, 1]])  # 뱀을 큐로 만들기
dir = 0 # 현재 뱀의 머리방향을 저장할 변수, 0: →, 1: ↓, 2: ←, 4: ↑
sec = 0

while True:
    sec += 1 # 게임 진행시간 증가
    newHead = deepcopy(snake[-1]) # 현재 뱀의 머리를 깊은 복사로 가져오기, 그냥 = 으로 가져옥면 snake 안에 값도 같이 바뀜
    
    # 현재 진행 방향 정보에 따라 뱀위의 머리위치 구하기
    if dir == 0:
        newHead[1] += 1
    elif dir == 1:
        newHead[0] += 1
    elif dir == 2:
        newHead[1] -= 1
    else:
        newHead[0] -= 1

    if newHead in snake: # 머리가 가야할 위치에 이미 뱀이 있다면 본인 몸과 닿는 것이므로 게임 종료
        # print('몸에 닿아서 게임종료 ', sec)
        print(sec)
        break

    if newHead[0] > N or newHead[1] > N or newHead[0] < 1 or newHead[1] < 1:
        # 뱀 머리가 보드를 나갔으면 게임 종료
        # print('게임종료 ', sec)
        print(sec)
        break

    snake.append(newHead) # 뱀 머리 업데이트

    isEat = False # 사과를 먹었는지 확인할 플래그
    for idx, apple in enumerate(apples):
        if apple == newHead: # 머리가 갈 위치에 사과가 있으면
            isEat = True # 플래그를 바꾸고
            apples = apples[:idx] + apples[idx + 1:] # 먹은 사과는 삭제
            break

    if not isEat: # 사과를 못먹었으면
        snake.popleft() # 뱀 꼬리칸 없애기

    if changes and int(changes[0][0]) == sec: # 방향 변환 정보가 남아있고 방향 변환 정보에 현재 초에 대한 정보가 있으면
        change = changes.popleft()
        if change[1] == 'D': # 오른쪽으로 90도 머리 회전
            dir += 1  # 현재 머리방향 업데이트
            dir %= 4  # 4로 나눈 나머지를 저장하면 0~3사이의 값 저장 가능
        else: # 왼쪽으로 90도 머리 회전
            dir += 3  # -1하는거랑 똑같은 연산
            dir %= 4