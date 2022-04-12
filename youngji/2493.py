#탑
import sys

n = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))

######## 시간초과 ##########
# n^2???

# index = []
# for i in range(n-1,-1,-1) :
#     for j in range(i-1,-1,-1) :
#         if top[j] > top[i] : 
#             index.append(str(j+1))
#             break
#     if len(index) < n-i :
#         index.append("0")
# index.reverse()

# # print(' '.join(index))
# print(*index)

# ######## 스택으로 풀어보자,,,,,,,

stack = []
answer = [0 for _ in range(n)]
for i in range(n) : 
    while stack : # stack이 없을때 까지 계속,,,
        if stack[-1][1] < top[i] :
            stack.pop()
        else : 
            answer[i] = stack[-1][0] + 1
            break
    stack.append([i,top[i]])
print(*answer)