import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
paper = []
total = [0, 0]

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().strip().split())))

def cutPaper(sx, sy, n):
    if n == 1:
        total[paper[sx][sy]] += 1
        return

    checked = [0, 0]
    for x in range(sx, sx + n):
        for y in range(sy, sy + n):
            checked[paper[x][y]] += 1

    box = n ** 2
    # print('cut paper ', sx, sy, n, checked, box)
    if checked[0] == box or checked[1] == box:
        total[paper[sx][sy]] += 1
        return

    nn = n // 2

    cutPaper(sx, sy, nn)
    cutPaper(sx, sy + nn, nn)
    cutPaper(sx + nn, sy, nn)
    cutPaper(sx + nn, sy + nn, nn)

cutPaper(0, 0, N)

for t in total:
    print(t)
