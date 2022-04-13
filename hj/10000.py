# 19. 원 영역
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
circles = []
for _ in range(N):
    [center, radius] = list(map(int, sys.stdin.readline().strip().split()))
	# 원 왼쪽점, 오른쪽점 담기
    circles.append([center - radius, center + radius])
circles.sort(key=lambda x:x[0]) # 왼쪽점 오름차순 정렬

points = []
for c in circles:
	# 왼쪽점, 오른쪽점 나눠서 points에 담기
    points.append(['L', c[0]]) 
    points.append(['R', c[1]])
points.sort(key=lambda x:x[1]) # 좌표 오름차순 정렬

area = 1 # 기본 영역 1

stack = []
for p in points:
    if p[0] == 'L':
        stack.append(p)  # 왼쪽 점이면 스택에 넣기
    else: # 오른쪽 점
        width = 0
        while stack:
            prev = stack.pop()
            if prev[0] == 'C':  # 이전에 완성된 원이 있으면 원의 지름 누적
                width += prev[1]
            elif prev[0] == 'L': 
                dia = p[1] - prev[1]
				# 왼쪽 점 만나면 누적 너비랑 자신의 지름이 같은지 확인
                if width == dia:
                    area += 2 # 같으면 원 내부가 다른 원들로 가득차서 반으로 갈라지므로 +2
                else:
                    area += 1 # 원내부가 안 채워졌으면 +1
                stack.append(['C', dia]) # 완성된 원 스택에 추가
                break
print(area)