num,point = map(int,input().split())
lev_list = []

for i in range(num):
    lev_list.append(int(input()))

lev_list.sort()

start = lev_list[0]
end = lev_list[num-1]

result = 0

while start <= end:
    sum_point = 0
    goal_lev = (start+end)//2

    for i in range(num):
        if lev_list[i] < goal_lev :
            sum_point += goal_lev - lev_list[i]
    
    if point >= sum_point:
        start = goal_lev+1
        result = goal_lev

    elif point < sum_point:
        end = goal_lev-1

    else:
        break

print(result)