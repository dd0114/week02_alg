from collections import deque
import sys

n = int(sys.stdin.readline()) #행, 열 개수
k = int(sys.stdin.readline()) # 사과개수
p = [sys.stdin.readline().split() for _ in range(k)] #사과위치
l = int(sys.stdin.readline()) # 이동 횟수
lline = [sys.stdin.readline().split() for _ in range(l)] #이동 리스트

count = 0
x,y = 1,1
bam = deque()
for i in range(l) :
    for j in range(int(i[0])) :
        if [x,y] in p : # 사과가 있을때 
            p.remove([x,y])
            # 길이 늘어나기?
        count += 1
        if x == n or y == n  :
            print(count)
            exit(0)

