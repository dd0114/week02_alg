from inspect import stack


def gh():
    a = input()
    r_sta = 0
    s_sta = 0
    ans_list =[]
    for i in range(len(a)):
        if a[i] == '(':
            r_sta += 1
            ans_list.append('(')

        elif a[i] == '[':
            s_sta += 1
            ans_list.append('[')

        elif a[i] == ')':
            r_sta -= 1
            if r_sta == -1 or ans_list[-1]=='[' :
                return(0)

            else :
                if ans_list[-1] == '(':
                    ans_list.pop()
                    ans_list.append(2)
                
                elif type(ans_list[-1]) == int :
                    b= 0
                    while ans_list[-1] != '(':
                        if ans_list[-1] == '[':
                            return(0)
                        b += ans_list.pop()
                    
                    ans_list.pop()
                    b *= 2
                    ans_list.append(b)
                else :
                    return (0)

        elif a[i] == ']':
            s_sta -= 1
            if s_sta == -1 or ans_list[-1] == '(':
                return(0)

            else :
                if ans_list[-1] == '[':
                    ans_list.pop()
                    ans_list.append(3)

                elif type(ans_list[-1]) == int :
                    b = 0
                    while ans_list[-1] != '[':
                        if ans_list[-1] == '(':
                            return(0)
                        b += ans_list.pop()
                    ans_list.pop()
                    b *= 3
                    ans_list.append(b)
                
                else :
                    return (0)
    return(sum(ans_list))
    

print(gh())