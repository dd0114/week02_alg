import sys
sys.stdin = open('input.txt')

[M, N, L] = list(map(int, sys.stdin.readline().strip().split()))
shots = list(map(int, sys.stdin.readline().strip().split()))
shots.sort()

animals = []

for _ in range(N):
    animals.append(list(map(int, sys.stdin.readline().strip().split())))

kill = 0

for animal in animals:
    if animal[1] > L:
        continue

    start = 0
    end = len(shots) - 1
    idx = 0
    diff = shots[-1] - shots[0]

    while start <= end:
        mid = (start + end) // 2
        shot = shots[mid]
        d = shot - animal[0]
        
        if abs(d) < diff:
            diff = abs(d)
            idx = mid

        if d < 0:
            start = mid + 1
        else:
            end = mid - 1

    shot = shots[idx]
    if (abs(shot - animal[0]) + animal[1]) <= L:
        kill += 1

print(kill)
