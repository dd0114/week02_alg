# 16. 괄호의 값
import sys

line = sys.stdin.readline().strip()
stack = [] # 괄호를 담을 스택
nums = []  # 계산 과정값을 저장 할 스택
result = 0 # 최종 연산값

for l in line:
    if l == '(':
        stack.append(l)
        nums.append(0)
    elif l == ')':
        if stack:
            p = stack.pop()
            ingN = nums.pop()
            if p == '[':  # 잘못된 괄호면 0출력하고 프로그램 종료
                print(0)
                exit(0)
            if nums: # 올바른 괄호면 계산 진행
                if ingN: nums[-1] += ingN * 2 # 계산 중이던 값이 있으면 해당 값에 2를 곱해서 nums탑값에 저장
                else: nums[-1] += 2 # 계산 중이던 값 없으면(0이면) nums 탑값에 2 더하기
            else: # 더 이상 계산 중인 값 없으면(stack 없으면, 괄호 짝이 다 맞았으면) 최종 연산값에 결과 더하기
                if ingN: result += ingN * 2
                else: result += 2
        else: # 짝이 없는 괄호면 0출력하고 프로그램 종료
            print(0)
            exit(0)
    elif l =='[':
        stack.append(l)
        nums.append(0)
    elif l ==']':
        if stack:
            p = stack.pop()
            ingN = nums.pop()
            if p == '(':
                print(0)
                exit(0)
            if nums:
                if ingN: nums[-1] += ingN * 3
                else: 
                    if nums[-1]: nums[-1] += 3
                    else: nums[-1] = 3
            else:
                if ingN: result += ingN * 3
                else: result += 3
        else:
            print(0)
            exit(0)

if stack: # 연산이 끝났는데 아직 짝을 못찾은 괄호가 있으면 잘못된 괄호이므로 0출력하고 프로그램 종료
    print(0)
    exit(0)

print(result)