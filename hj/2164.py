# 21. 카드2
import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for n in range(1, N + 1):
    queue.append(n)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())