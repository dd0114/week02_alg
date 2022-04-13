import sys
sys.stdin = open('input.txt')

def largest(arr):
    stack = []
    maxArea = 0
    for n in arr[1:]:
        w = 0
        while stack and stack[-1][0] >= n:
			# 스택에는 현재까지 오름차순으로 히스토그램이 담겨있다.
            w += stack[-1][1] # 밑변 길이 누적
            maxArea = max(maxArea, w * stack[-1][0]) # 현재 최대 넓이랑 밑변*스택탑값 비교해서 최대넓이 갱신
            stack.pop()
        w += 1
        stack.append([n, w])  # 새로운 숫자 넣을 때 그동안 누적된 밑변값으로 넣어줌
    w = 0
    while stack:  # 스택에 남아있는 값들도 처리해줌
        w += stack[-1][1]
        maxArea = max(maxArea, w * stack[-1][0])
        stack.pop()
    return maxArea


while True:
    line = list(map(int, sys.stdin.readline().strip().split()))
    if line[0] == 0:
        break
    print(largest(line))