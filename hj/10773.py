# 13. 제로
import sys

inputN = int(sys.stdin.readline())
stack = []

for _ in range(inputN):
    n = int(sys.stdin.readline())

    if n:
        stack.append(n)
    else:
        stack.pop()

total = 0

for n in stack:
    total += n

print(total)