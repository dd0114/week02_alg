# 12. 스택
import sys
sys.stdin = open('input.txt')

lineN = int(sys.stdin.readline())
lines = []
stack = []

for _ in range(lineN):
    line = sys.stdin.readline().strip().split()
    lines.append(line)

def command(line):
    c = line[0]

    if c == 'push':
        stack.append(int(line[1]))
    elif c == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif c == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    elif c == 'size':
        print(len(stack))
    else:
        if stack:
            print(0)
        else:
            print(1)

for line in lines:
    command(line)

    