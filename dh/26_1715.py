import heapq
import sys

n = int(input())
num_list = []
count = 0

for i in range(n):
    heapq.heappush(num_list,int(sys.stdin.readline()))

for i in range(n-1):
    a = heapq.heappop(num_list)+heapq.heappop(num_list)
    heapq.heappush(num_list,a)
    count += a

print(count)

