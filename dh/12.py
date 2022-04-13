# 10828 번
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
import sys

n = int(input())
stack = []

for i in range(n) :
    s = sys.stdin.readline().split()

    if s[0] == "push" :
        stack.append(s[1])
    
    if s[0] == "pop" :
        if len(stack)==0 :
            print(-1)

        else:
            print(stack.pop())

    if s[0] == "size":
        print(len(stack))
    
    if s[0] == "empty":
        if len(stack) == 0:
            print(1)
        else :
            print(0)
    
    if s[0] == "top":
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)