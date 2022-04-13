import heapq
import sys

n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]

sheap = [] #최대힙
bheap = [] #최소힙
for i in range(n) :
    if len(sheap) == len(bheap)+1 :
        heapq.heappush(bheap,num[i])
    else :
        heapq.heappush(sheap,(-num[i],num[i]))
    
    if len(bheap) > 0 :
        if bheap[0] < sheap[0][1] :
            a = heapq.heappop(bheap)
            b = heapq.heappop(sheap)[1]

            heapq.heappush(sheap,(-a,a))
            heapq.heappush(bheap,b)
    
    print(sheap[0][1])

