import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
dots = []
for _ in range(N):
    dots.append(list(map(int, sys.stdin.readline().strip().split())))
dots.sort() # 점들 x축 기준으로 정렬


def distDots(dot1, dot2):
    return (dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2

def calcDist(s, e): # 3개 이하의 점이 주어졌을 때 최소 간격 반환하는 함수
    result = distDots(dots[s], dots[e])
    for i in range(s, e):
        for j in range(i + 1, e + 1):
            dist = distDots(dots[i], dots[j])
            if result > dist:
                result = dist
    return result

def minDist(start, end):
    if end - start < 3: # 나누다가 점이 3개 이하가 되면 최소 거리 반환
        return calcDist(start, end)

    mid = (start + end) // 2
    minD = min(minDist(start, mid), minDist(mid, end)) # 양쪽 구간에서 나온 최소 거리들 중 더 작은것을 minD로 설정

    temp = []  # 가까운 점 후보들을 담을 배열

    for i in range(start, end):
        xd = dots[i][0] - dots[mid][0]  # x좌표의 차이 구하기
    
        if xd * xd < minD:  # x 좌표 차이가 최소거리 이내이면 후보군에 넣기
            temp.append(dots[i])
    temp.sort(key=lambda x:x[1])   # y좌표 기준으로 정렬

    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            y = temp[j][1] - temp[i][1]
            if y * y < minD:  # y좌표 차이가 최소거리보다 작으면 두점사이 거리 구하기
                dist = distDots(temp[j], temp[i])
                if dist < minD: # 두 점 사이거리가 최소거리보다 작으면 최소거리 업데이트
                    minD = dist
            else:
                break
    return minD
    
print(minDist(0, N-1))