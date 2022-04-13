# # 큐2
from collections import deque
import sys

queue = deque([])
n = int(sys.stdin.readline())
case = [sys.stdin.readline().split() for _ in range(n)]

for i in case :
    m = i[0]
    if m == 'push' :
        queue.append(i[1])
    elif m == 'pop' :
        if len(queue) :
            print(queue.popleft())
        else : print(-1)
    elif m == 'size':
        print(len(queue))
    elif m == 'empty':
        if len(queue) : print(0)
        else : print(1)
    elif m == 'front':
        if len(queue) : 
            print(queue[0])
        else : print(-1)
    elif m == 'back':
        if len(queue) : print(queue[-1])
        else : print(-1)

