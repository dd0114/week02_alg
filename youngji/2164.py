from collections import deque
import sys
n = int(sys.stdin.readline())

card = deque([])
for i in range(1,n+1) :
    card.append(i)

if len(card) :
    while 1 :  
        if len(card) == 1 :
            print(card.pop())
            exit(0)  
        card.popleft()
        temp = card.popleft()
        card.append(temp)
        

