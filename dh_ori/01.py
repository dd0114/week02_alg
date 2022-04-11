from posixpath import split

N = int(input())
nlist = list(map(int,input().split()))
M = int(input())
mlist = list(map(int,input().split()))

nlist = sorted(nlist)

def find(n) :
    pl = 0
    pr = N-1

    while pl <= pr :
        pc = (pl+pr)//2
        if n == nlist[pc] :
            return True
    
        elif n > nlist[pc] :
            pl = pc +1
        
        else  :
            pr = pc -1

for i in range(M):
    if find(mlist[i]):
        print(1)
    else:
        print(0) 