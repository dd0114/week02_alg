# 26. 카드 정렬하기
import sys
import heapq

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = []
total = 0

for _ in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(nums, num)

while len(nums) > 1: # 힙에서 원소 두개 pop해야하니까 배열 길이가 2이상이면 반복
    num1 = heapq.heappop(nums)
    num2 = heapq.heappop(nums)
	# 가장 작은 숫자 두개 뽑아서 더하고
    cost = num1 + num2
    total += cost # 결과값에 연산값 더하기

    heapq.heappush(nums, cost) # 가장 작은 숫자 두개 연산한 값 최소 힙에 넣기
    # print('n1 + n2 ', num1, num2, num1 + num2)

print(total)