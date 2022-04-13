from collections import deque

n, k = map(int,input().split())
num_list = deque([])

for i in range(n):
    num_list.append(i+1)

print ('<',end='')

for i in range(n-1) :
    for j in range(k-1):
       num_list.append(num_list.popleft())
    
    print(f'{num_list.popleft()}, ',end='')

print(f'{num_list.popleft()}>')
