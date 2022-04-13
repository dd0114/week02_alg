import heapq
import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

heapq.heapify(nums)
allsum = 0
while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    sum = a+b
    allsum += sum
    heapq.heappush(nums,sum)

print(allsum)
