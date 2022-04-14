# 가운데르르 말해요
import sys
import heapq

maxheap =[]
minheap =[]

n = int(input())
minheap.append(int(input()))

if len(minheap) == 1:
    print(minheap[0])

for i in range(n-1):
    
    a = int(sys.stdin.readline())
    
    if a >= minheap[0]:
        heapq.heappush(minheap,a)
    else :
        heapq.heappush(maxheap,a*-1)

    if len(maxheap) == len(minheap):
        b = heapq.heappop(maxheap)
        heapq.heappush(minheap,b*-1)
    elif len(maxheap) - len(minheap) == - 3 :
        c = heapq.heappop(minheap)
        heapq.heappush(maxheap,c*-1)

    print(minheap[0])

# 최대힙과 최소힙을 만든다.
####
# 아무것도 없으면 최소힙에 넣는다.

# 최소힙과 비교해서 더 크면 최소힙에 넣는다.
# 더 작으면 최대 힙에 넣는다.

###

# 최대힙과 최소힙 길이를 비교한다. 높이가 같으면 최대힙에서 힙팝으로 최소힙으로 힙푸쉬한다.
# 높이가 3개 차이나면 최소힙에서 힙팝 -> 최대힙으로 힙푸쉬 

# 최소힙의 0번값을 프린트한다.