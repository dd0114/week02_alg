s,d,l = map(int,input().split())

s_list = list(map(int,input().split()))

d_xy = []

for i in range(d):
    d_xy.append(list(map(int,input().split())))
s_list.sort()
d_xy.sort()
count = 0

start = 0
end = s-1

def kill(x,y):
    start = 0
    end = s-1

    while start <= end:
        mid = (start+end) //2
        if abs(x - s_list[mid])+y <= l:
            return True

        elif x > s_list[mid] :
            start = mid+1
        elif x < s_list[mid] :
            end = mid-1
        else :
            return False

for i in range(d):
    if kill(d_xy[i][0], d_xy[i][1]):
        count += 1

print(count)