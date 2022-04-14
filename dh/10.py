from collections import deque

while True :
    n = list(map(int,input().split()))
    
    if n ==[0]:
        exit(0)

    stack = []
    maxbox = 0
    length = 0

    for i in range(1,len(n)):
        length = i
        while stack and n[i] < n[i-1] :
            a = stack.pop()
            if len(stack) == 0:
                ptr = n[a]*(length-1)
            else:
                ptr = n[a]*(length-a)
            if ptr > maxbox:
                maxbox = ptr

        stack.append(i)

    while stack :
        a = stack.pop()
        if len(stack) == 0:
            ptr = n[a]*(length)
        else:
            ptr = n[a]*(length-a+1)
        if ptr > maxbox:
                maxbox = ptr

    print(maxbox)