#크게 만들기

import sys

n,k = map(int,sys.stdin.readline().split())
s = list(map(int,sys.stdin.readline().strip()))

l = n-k
stack = []

for i in range(n) :
    while k > 0 and stack :
        if stack[-1] < s[i] :
            stack.pop()
            k -= 1
        else : break
    if len(stack) < l : stack.append(s[i])

print(''.join(str(x) for x in stack))
# 이게 되겠냐
