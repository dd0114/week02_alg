N, M = map(int,input().split())
tree = list(map(int,input().split()))

r,l = max(tree),0

while l <= r :
    c = (l+r)//2
    hap = 0

    for i in tree:
        if i> c:
            hap += i-c

    if hap >= M :   
        l = c+1
    else : # hap < M:
        r = c-1


print(r)
