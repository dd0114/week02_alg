N, M = map(int,input().split())
tree = list(map(int,input().split()))

tree = sorted(tree)

r = tree[N-1]
l = tree[0]
hap = 0

while l <= r :
    c = (l+r)//2
    hap = 0

    for i in range(N):
        if tree[i]-c <0:
            hap += 0
        else:    
            hap += tree[i]-c


    if hap < M:
        r = c+1

    else : #hap >= M :   
        l = c-1


print(c)
