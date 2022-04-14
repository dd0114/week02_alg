import sys
import heapq

n = int(input())

a = []

for i in range(n):
    num = int(sys.stdin.readline())

    if num == 0 :
        if a:
            print((heapq.heappop(a))*-1)
        else :
            print(0)

    else :
        heapq.heappush(a,-num)
