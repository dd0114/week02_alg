n = int(input())
ylist = list(map(int,input().split()))

ylist = sorted(ylist)

s = 0
e = n-1

save_left = ylist[0]
save_right = ylist[n-1]
save_nongdo = ylist[0]+ylist[n-1]

start = ylist[s]
end = ylist[e]

while s < e :
    start = ylist[s]
    end = ylist[e]
    nongdo = start + end

    if abs(nongdo) < abs(save_nongdo) :
        save_nongdo = nongdo
        save_left = start
        save_right = end
    
    if nongdo >0 :
        e -= 1    
    elif nongdo <0:
        s += 1
    else:
        break

    
print (save_left, save_right)