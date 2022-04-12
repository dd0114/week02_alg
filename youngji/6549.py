#히스토그램
#개망

import sys

hlist = []
while 1 :
   t = sys.stdin.readline().strip()
   if t == '0' :
        break
   else :
       n,*h = t.split()
       hlist.append(h)

# print(hlist)

def sol(arr) :
    width = 1
    stack = []
    max_area = 0
    for i in range(len(arr)) :
        if arr[i] > arr[i-1] :
            if arr[i] > max_area :
                max_area = arr[i]
                stack = [arr[i]]
            else : 
                max_area = max_area//len(stack)*(len(stack)+1)
                stack.append(arr[i])
                
        elif arr[i] < arr[i-1] :
            if arr[i] * (len(stack)+1) > max_area :
            max_area = arr[i] * len(stack)
            stack.append(arr[i])



for arr in hlist :
    arr = [int(x) for x in arr]
    sol(arr)
