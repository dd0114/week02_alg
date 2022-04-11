from tkinter import N


n, c = map(int,input().split())
house = [0] * n

for i in range(n):
    house[i] = int(input())

house = sorted(house)


start = 1
end = house[n-1] - house[0]
result = 0
# 올드는 초기화 되어야한다. 

if c==2 :
    print(house[1] - house[0])

else :
    while start <= end :
        count = 1
        mid = (start+end)//2
        old = house[0]

        for i in range(1,n):
            if house[i]-old >= mid :
                count +=1
                old = house[i]

        if count >= c :
            start = mid+1
        
        else : # count < c :
            end = mid-1

    print(mid)