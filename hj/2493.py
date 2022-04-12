# 17. 탑
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

towers = list(map(int, sys.stdin.readline().strip().split()))
result = [0] * N
stack = []

for idx, tower in enumerate(towers):
    if not stack: # 빈 스택이면 값을 추가한다.
        stack.append([idx, tower])
        continue
    while stack and stack[-1][1] < tower: # 만약 현재 타워의 높이가 스택의 top값보다 크다면
        popT = stack.pop() # 스택에 있던 값을 pop
		# 현재 타워의 높이가 스택의 top보다 작거나 같으면 while문 탈출

    if stack:
		# 스택에 값이 남아있으면 제일 가까운 본인보다 높은 타워이므로 해당 타워의 순서(인덱스 + 1)를 result에 추가한다
        result[idx] = stack[-1][0] + 1
    else:
		# 본인보다 높은 타워가 없으면 0넣기
        result[idx] = 0
    stack.append([idx, tower]) # 현재 타워를 스택에 추가한다


print(' '.join(list(map(str, result))))
