# 15. 막대기
import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    stack.append(int(sys.stdin.readline()))

top = stack.pop()
count = 1

while stack:
    popN = stack.pop()
    if popN > top:
        top = popN
        count += 1

print(count)

