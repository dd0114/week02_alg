import math
x = int(input())
a = [[*map(int,input().split())] for _ in range(x)]

a.sort()
# print(a)
mini = math.pow(a[0][0]-a[1][0],2) + math.pow(a[0][1]-a[1][1],2)

for i in range(len(a)-1):
    if mini > math.pow(a[i][0]-a[i+1][0],2) + math.pow(a[i][1]-a[i+1][1],2):
        mini = math.pow(a[i][0]-a[i+1][0],2) + math.pow(a[i][1]-a[i+1][1],2)

def sol(x,y) : #x,y는 각각 위치 좌표 - 일차배열
    global mini
    #길이가 mini 보다 작은지 확인
    if  math.pow(x[0]-y[0],2) + math.pow(x[1]-y[1],2) < mini :
        return True
    return False

def dis() :
    global mini
    for z in range(len(a)) :
        i = a[z]
        for j in range(z+1,len(a)) :
            if a[j][0] <= i[0] + int(math.sqrt(mini)) :
                if sol(i,a[j]) :
                    mini = math.pow(i[0]-a[j][0],2) + math.pow(i[1]-a[j][1],2)
                    if mini == 0 : return
    
dis()
print(int(mini))