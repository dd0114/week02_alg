# 14. 괄호
import sys
sys.stdin = open('input.txt')

lineN = int(sys.stdin.readline())
lines = []

for _ in range(lineN):
    lines.append(sys.stdin.readline().strip())

for line in lines:
    stack = []

    for l in line:
        if l == '(':
            stack.append(l)
        else:
            if stack:
                stack.pop()
            else: # 잘못된 괄호, 짝이 없는 괄호
                stack.append(l)
                break

    if stack:   
        print('NO')
    else:
        print('YES')