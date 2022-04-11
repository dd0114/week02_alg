import sys
sys.stdin = open('input.txt')

[N, M] = list(map(int, sys.stdin.readline().strip().split()))
trees = list(map(int, sys.stdin.readline().strip().split()))
trees.sort()
start = 0
end = trees[-1]
minDiff = 1000000000
diffH = 0

# print(trees)

def sumTrees(height):
    total = 0
    for h in trees:
        cut = h - height
        if cut > 0:
            total += cut
    # print('sum trees ', height, total)
    return total

def binarySearch(start, end):
    global minDiff
    global diffH

    # print('start ', start, end)
    if start > end:
        return diffH

    if start == end:
        if M == sumTrees(start):
            return start

    midH = (start + end) // 2
    cut = sumTrees(midH)

    if M == cut:
        return midH

    if M < cut:
        if cut < minDiff:
            minDiff = cut
            diffH = midH
        # print('더 적게')
        return binarySearch(midH + 1, end)
    else:
        # print('더 많게')
        return binarySearch(start, midH - 1)

print(binarySearch(start, end))
