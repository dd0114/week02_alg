# 24. 최대 힙
import sys
import heapq

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    
    if num:
		# heapq 모듈은 기본적으로 최소힙을 만들게 되어있음
        heapq.heappush(heap, (-num, num)) # 최대힙을 만들기 위해 음수를 붙인 숫자를 튜플에 담아 넣기
		# 이렇게 담으면 첫번째 원소 기준으로 최소힙을 만드니까 결론적으로 최대힙이 만들어짐
    else:
        if heap:
            print(heapq.heappop(heap)[1]) # 사용할 때는 원래 원소값이 튜플의 1번 인덱스 가져와서 사용
        else:
            print(0)