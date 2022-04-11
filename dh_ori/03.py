from tkinter import N


n, c = map(int,input().split())
house = [0] * n

for i in range(n):
    house[i] = int(input())

house = sorted(house)
dab = [0]*c
dab[c-1] = n-1

dab[1] = 2
# for i in range(c-2,1,-1):
#     dab[i] = i

ans = 1000000
new = 100000

while new < ans :
    ans = new

    for i in range(1,c-1):
        mid = dab[i-1] + dab[i+1] //2
        left = dab[i-1]
        right = dab[i+1]

        ori = max(abs(house[left]-house[dab[i]]), abs(house[dab[i]]-house[right]))
        new = max(abs(house[left]-house[mid]), abs(house[mid]-house[right]))

        if new < ori :
            dab[i]=mid  
        else :
            new = ori        

print(ans)
        