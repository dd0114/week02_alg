n = int(input())

stack =[]

for i in range(n):
    s = int(input())

    if s != 0 :
        stack.append(s)
    
    else :
        stack.pop()

print(sum(stack))