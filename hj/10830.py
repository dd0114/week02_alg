import sys
sys.stdin = open('input.txt')

[N, B] = list(map(int, sys.stdin.readline().strip().split()))
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

def multi(arr1, arr2, n):
    result = []
    for n1 in range(n):
        result.append([])
        for n2 in range(n):
            calc = 0
            for idx, n3 in enumerate(arr1[n1]):
                calc += n3 * arr2[idx][n2]
                # print(f'result[{n1}][{n2}]({calc}) += {n3} x {arr2[idx][n2]} = {n3 * arr2[idx][n2]}')
            result[n1].append(calc % 1000)
    
    # print('result ', result)
    return result

def powMatrix(arr, n):
    # print('pow ', arr, n)
    if n == 0:
        return 1

    if n == 1:
        return arr

    if n % 2:
        return multi(arr, powMatrix(arr, n - 1), N)
    else:
        temp = powMatrix(arr, n // 2)
        return multi(temp, temp, N)
        
        
# multi([[1, 2], [3, 4]], [[1, 2], [3, 4]], 2)
result = powMatrix(arr, B)
for r in result:
    newR = []
    for rr in r:
        newR.append(rr % 1000)
    print(' '.join(map(str, newR)))