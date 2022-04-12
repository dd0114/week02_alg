# 막대기

import sys
n = int(sys.stdin.readline())
h = [int(sys.stdin.readline()) for _ in range(n)]

max = h[n-1]
result = [max]
# 맨뒤 막대기를 기준으로 잡은후 뒤에서부터 반복문을 돌리면서 더 큰수만 추가
for i in range(n-2,-1,-1) :
    if h[i] > max :
        max = h[i]
        result.append(max)
    else : continue

print(len(result))
