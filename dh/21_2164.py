from collections import deque

n = int(input())

cardlist = deque([])

for i in range(n):
    cardlist.append(i+1)


while len(cardlist) > 1 :
    cardlist.popleft()
    cardlist.append(cardlist.popleft())

print(cardlist[0])
