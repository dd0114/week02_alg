# 26. 요세푸스 문제 0
import sys

[N, K] = list(map(int, sys.stdin.readline().strip().split()))
K -= 1
circle = [n for n in range(1, N + 1)]
result = []
end = 0

while len(result) < N:
    count = end + K
    if len(circle) > count:
        result.append(circle[count])
        end = count
        circle = circle[:count] + circle[count+1:]
    else:
        idx = (count % len(circle))
        result.append(circle[idx])
        end = idx
        circle = circle[:idx] + circle[idx+1:]

ans = '<'
ans += ', '.join(list(map(str, result)))
ans += '>'
print(ans)