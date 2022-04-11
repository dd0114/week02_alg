import sys
sys.stdin = open('input.txt')

[N, K] = list(map(int, sys.stdin.readline().strip().split()))

levels = []
for _ in range(N):
    levels.append(int(sys.stdin.readline()))
levels.sort()

start = levels[0]
end = levels[-1] + (K // N)

def sumLevelUp(goal):
    total = 0
    for level in levels:
        up = goal - level
        if up > 0 :
            total += up
    return total

def maxLevel(s, e):
    mid = (s + e) // 2
    total = sumLevelUp(mid)

    if s > e:
        return mid
    
    if total == K:
        return mid

    if total > K:
        return maxLevel(s, mid - 1)
    else:
        return maxLevel(mid + 1, e)
        
print(maxLevel(start, end))