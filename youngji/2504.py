# 괄호의 값
import sys

s = sys.stdin.readline().strip()
stack = []
temp = 1
sum = 0
for i in range(len(s)) :
    if s[i] == '(' :
        stack.append(s[i])
        temp *= 2
    elif s[i] == '[' :
        stack.append(s[i])
        temp *= 3
    elif s[i] == ')' :
        if not stack or stack[-1] == '['  : #이거 반대로 했더니 인덱스에러 남
            sum = 0
            break
        elif s[i-1] == '(' :
            sum += temp
        stack.pop()
        temp //= 2 
    elif s[i] == ']' :
        if not stack or stack[-1] == '(' : 
            sum = 0
            break
        elif s[i-1] == '[' :
            sum += temp
        stack.pop()
        temp //= 3
    # print(stack)

if stack : #괄호 짝이 다 맞으면 stack이 비어야함
    print(0)
else : 
    print(sum)