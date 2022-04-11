import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

liquids = list(map(int, sys.stdin.readline().strip().split()))
liquids.sort()

start = 0
end = len(liquids) - 1
minSum = 10000000000
minS = liquids[0]
misE = liquids[-1]

while start < end:
    add1 = liquids[start]
    add2 = liquids[end]

    sum2 = add1 + add2

    if sum2 == 0:
        print(f'{add1} {add2}')
        exit(0)

    if abs(sum2) < minSum:
        minSum = abs(sum2)
        minS = add1
        minE = add2

    if sum2 > 0:
        end -= 1
    else:
        start += 1

print(f'{minS} {minE}')




