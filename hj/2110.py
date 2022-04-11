import sys
sys.stdin = open('input.txt')

[N, C] = list(map(int, sys.stdin.readline().strip().split()))

houses = []
for _ in range(N):
    houses.append(int(sys.stdin.readline()))
houses.sort()

result = 1

def binary_search(start, end):
    global result

    mid = (start + end) // 2
    if start > end:
        return

    count = 1
    pin = houses[0]

    for idx in range(1, len(houses)):
        dist = houses[idx] - pin
        if dist >= mid:
            count += 1
            pin = houses[idx]

    if count >= C:
        # print('공유기가 많다 간격을 넓히자', count, C, mid)
        result = mid
        return binary_search(mid + 1, end)
    else:
        # print('공유기가 적다 간격을 좁히자', count, C, mid)
        return binary_search(start, mid - 1)

binary_search(1, (houses[-1] - houses[0]))    
print(result)