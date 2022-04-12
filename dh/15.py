# 17608번 막대기
n = int(input())

stack = []

for i in range(n):
    m = int(input())

# 앤드문은 둘중에 앞에 거를 먼저 판단
    while stack and m >= stack[-1] :
        stack.pop()

    stack.append(m)

print(len(stack))