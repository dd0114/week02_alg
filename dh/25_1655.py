# 가운데를 말해요. 시간초과남
import heapq
import sys
import copy

n = int(input())
alist = []

for i in range(n):
    b = int(sys.stdin.readline())
    heapq.heappush(alist,b)
    clist = copy.deepcopy(alist)

    for j in range(i//2):
        heapq.heappop(clist)
    
    print(heapq.heappop(clist))
