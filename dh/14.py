n = int(input())

for i in range(n):
    s = input()
    stack = 0
    for j in range(len(s)):
        if s[j] == "(" :
            stack += 1
        else :
            stack -=1
            if stack == -1:
                break
    
    if stack == 0:
        print("YES")
    else:
        print("NO")