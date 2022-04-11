import sys
[A, B, C] = list(map(int, sys.stdin.readline().strip().split()))

def pow(a, b, c):
    # print('pow ', a, b)
    if b == 0:
        return 1

    if b == 1:
        return a % c

    if b % 2:
        return (a * pow(a, b - 1, c)) % c
    else:
        half = pow(a, b // 2, c)
        return (half * half) % c

print(pow(A, B, C))
