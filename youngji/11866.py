# 요세푸스 문제 0

from collections import deque
import sys

n,k = map(int,sys.stdin.readline().split())

person = deque()
for i in range(1,n+1) :
    person.append(str(i))

result =[]
#원형큐 사용하기ㄴ
while person :
    person.rotate(-k+1)
    result.append(person.popleft())


print('<',end='')
print(', '.join(result),end='')
print('>')