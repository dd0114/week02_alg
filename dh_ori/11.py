x = int(input())
a = [[*map(int,input().split())] for _ in range(x)]

a.sort()
# print(a)
mini = (a[0][0]-a[1][0])**2 + (a[0][1]-a[1][1])**2

def sol(x,y) : #x,y는 각각 위치 좌표 - 일차배열
    global mini
    #길이가 mini 보다 작은지 확인
    if  (x[0]-y[0])**2 + (x[1]-y[1])**2 < mini :
        return True
    
# return False

def dis() :
    global mini
    for i in range(len(a)-1):
        k=1
        while True :
            if len(a)-1 <i+k or (a[i][0]-a[i+k][0])**2 < mini :
                break
            
            if (a[i][0]-a[i+k][0])**2 + (a[i][1]-a[i+k][1])**2 < mini :
                mini = (a[i][0]-a[i+k][0])**2 + (a[i][1]-a[i+k][1])**2

            k  += 1

        #  넘어서면 깨지게
dis()
print(int(mini))



# x 좌표로 모든점 소팅

# x[left] x[right]

# left = 0
# right = 1

# 1. 레프트와 라이트 차이가 1이면 라이트를 한칸이동
# 2. right 가 max면 레프트를 이동
# 3. [left+1]과 right 와 left 와 right 의 y값 차이를 비교
# 4. 전자가 짧을경우 left += 1
# 5. 후자일경우 right +=

# y축으로 정렬도 필요할까?
# 하면 안전할거같은데

# 풀기전 논리집합 정리해서 생각해보깉