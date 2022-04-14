# 철로. 시간초과
import heapq
import sys

from setuptools import PEP420PackageFinder
n = int(input())

people = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if a < b :
        heapq.heappush(people,(a,b))
    else :
        heapq.heappush(people,(b,a))

people = sorted(people)
d = int(input())

now = []
alt = []
maximum = 0

while people :
    loc = people[0][0]
    while people and loc<= people[0][0] <= loc+d :
        a = heapq.heappop(people)
        if not a[1]-a[0] > d:
            if a[1] <= loc+d :
                heapq.heappush(now,a)
            else :
                heapq.heappush(alt,a)
    
    while now and now[0][0] < loc:
        heapq.heappop(now)
    
    if maximum < len(now):
        maximum = len(now)
    
    while alt :
        c = heapq.heappop(alt)
        heapq.heappush(people,c)

print(maximum)
