# 1224. [S/W 문제해결 기본] 6일차 - 계산기3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14tDX6AFgCFAYD
import sys
sys.stdin = open('res/input_1224.txt', 'r')

icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}


def operate(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v1 // v2


for tc in range(1, 11):
    N = int(input())
    lst = list(input().strip())
    postfix = []
    stack = []
    for l in lst:
        if l.isdigit():
            postfix.append(l)
        elif l == ')':
            while stack and stack[-1] != '(':
                v = stack.pop()
                postfix.append(v)
            stack.pop()
        else:
            while stack and isp[stack[-1]] >= icp[l]:
                v = stack.pop()
                postfix.append(v)
            stack.append(l)
    
    while stack:
        v = stack.pop()
        postfix.append(v)

    

    stack = []
    for i in postfix:
        if i.isdigit():
            stack.append(i)
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(operate(int(v1), int(v2), i))


    print(f'#{tc}', *stack)