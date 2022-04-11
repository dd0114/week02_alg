import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arrN = list(map(int, sys.stdin.readline().strip().split()))
arrN.sort()

M = int(sys.stdin.readline())
arrM = list(map(int, sys.stdin.readline().strip().split()))

def binarySearch(n, start, end):
    if start > end:
        return 0

    if start == end:
        if n == arrN[start]:
            return 1
        return 0

    midIdx = (start + end) // 2
    midNum = arrN[midIdx]

    if n == midNum:
        return 1

    if n > midNum:
        return binarySearch(n, midIdx + 1, end)
    else:
        return binarySearch(n, start, midIdx - 1)

for m in arrM:
    print(binarySearch(m, 0, len(arrN) - 1))