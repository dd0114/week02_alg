# 18. 크게 만들기
import sys
sys.stdin = open('input.txt')

[N, K] = list(map(int, sys.stdin.readline().strip().split()))

nums = sys.stdin.readline().strip()
stack = []
cnt = 0

for num in nums:
    if not stack:
        stack.append(num)
        continue

    while stack and stack[-1] < num and cnt < K:
        stack.pop()
        cnt += 1

    stack.append(num)

print(''.join(stack[:N - K])) # 출력 길이만큼 잘라서 출력
