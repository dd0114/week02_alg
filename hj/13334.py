# 27. 철로
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
people.sort(key=lambda x: x[1])  # 최종적으로 도착지 기준으로 정렬
D = int(sys.stdin.readline())

queue = []
maxLen = 0

for i in people:
    start = i[0]
    end = i[1]

    if end - start <= D:  # 출발지와 도착지 사이거리가 철로길이 D이하이면 최소힙에 넣기
        heapq.heappush(queue, i)
        
    while queue:
        if end - queue[0][0] <= D: 
		# 최소힙의 탑값(출발지가 가장 앞에있는 원소)의 출발지가 현재 도착지와 D간격 이내에 있으면 while문 탈출, 최소힙 안에있는 모든 원소는 철도 안에 있음
            break
        else:
		# 출발지가 철도길이 D밖에 있으면 pop하고 계속 while문 실행
            heapq.heappop(queue)
    qLen = len(queue)

    if maxLen < qLen:  # 현재 최소힙의 크기가 maxLen보다 크면 값 갱신
        maxLen = qLen
    
print(maxLen)

# 각각의 원소를 오름차순으로 정렬(집, 사무실 상관없음)
# 전체적으로 for문은 도착지 오름차순이고 최소힙은 출발지 오름차순인게 중요!