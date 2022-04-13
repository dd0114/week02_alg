import heapq
import sys
n = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for _ in range(n)]
result = []

for i in x :
    if i == 0 : 
        if result : print(heapq.heappop(result)[1])
        else : print(0)
    else : 
        heapq.heappush(result,(-i,i))

