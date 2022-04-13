import sys
import heapq
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
people = []

for _ in range(N):
    info = list(map(int, sys.stdin.readline().strip().split()))
    if info[0] > info[1]:
				# 어디가 집이고 사무실인지는 중요x, 작은 좌표를 앞에 큰 좌표를 뒤에
        info = [info[1], info[0]]
    people.append(info)
people.sort() # 출발지 기준 정렬
D = int(sys.stdin.readline())

queue = []
maxLen = 0

while people:
    i = people.pop()
    start = i[0]
    end = i[1]

    if end - start <= D:  # 출발지와 도착지 사이거리가 철로길이 D이하이면 최소힙에 넣기
        # heapq.heappush(queue, i)
        heapq.heappush(queue, (-i[1], i))
    while queue:
        if queue[0][1][1] <= start + D:
			# 최소힙의 탑값(도착지가 가장 뒤에 있는 원소)의 도착지가 현재 출발지와 D간격 이내에 있으면 while문 탈출, 최소힙 안에있는 모든 원소는 철도 안에 있음
            break
        else:
			# 도착지가 철도길이 D밖에 있으면 pop하고 계속 while문 실행
            heapq.heappop(queue)
    qLen = len(queue)

    if maxLen < qLen:  # 현재 최소힙의 크기가 maxLen보다 크면 값 갱신
        maxLen = qLen
    
    
print(maxLen)