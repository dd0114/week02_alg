# 25. 가운데를 말해요
import sys
import heapq
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
maxHeap = []
minHeap = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if not maxHeap:
        heapq.heappush(maxHeap, (-num, num))  # 최대 힙이 비어있으면 최대힙에 숫자 넣기
    else:
        if len(maxHeap) > len(minHeap):  # 최대힙이 최소힙보다 크면 최소힙에 숫자 넣기
            heapq.heappush(minHeap, num)
        else:
            heapq.heappush(maxHeap, (-num, num))

        if maxHeap[0][1] > minHeap[0]:  
			# 최대힙의 탑값(절반 중 가장 큰 수)가 최소힙의 탑값(나머지 절반 중 가장 작은 수) 보다 크면
            minTop = heapq.heappop(minHeap)
            maxTop = heapq.heappop(maxHeap)
						# 최대힙과 최소힙 탑값 교환
            heapq.heappush(minHeap, maxTop[1])
            heapq.heappush(maxHeap, (-minTop, minTop))

    # 이렇게 정렬하면 입력된 숫자들 중 작은 숫자 절반은 최대힙에, 큰 숫자 절반은 최소힙에 들어간다
	# 여기서 최대힙 루트값을 보면 지금까지 입력된 숫자들중 중간값 or 중간값 중 앞에 값을 가져올 수 있다
    print(maxHeap[0][1])