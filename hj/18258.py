# 20. 큐 2
import sys
from collections import deque

sys.stdin = open('input.txt')

inputN = int(sys.stdin.readline())
lines = []
queue = deque()

def commandQueue(arr):
    global queue
    command = arr[0]

    if command == 'push':
        queue.append(arr[1])
    elif command == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

for _ in range(inputN):
    commandQueue(sys.stdin.readline().strip().split())