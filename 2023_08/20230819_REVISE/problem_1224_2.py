# 1224. [S/W 문제해결 기본] 6일차 - 계산기3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14tDX6AFgCFAYD
import sys
sys.stdin = open('res/input_1224.txt', 'r')

def operate(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v1 // v2

icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

for tc in range(1, 11):
    N = int(input())
    infix = list(input().strip())

    postfix = []
    stack = []
    for i in infix:
        if i.isdigit():
            postfix.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and isp[stack[-1]] >= icp[i]:
                postfix.append(stack.pop())
            stack.append(i)

    while stack:
        postfix.append(stack.pop())

    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(operate(v1, v2, i))
    
    print(f'#{tc}', *stack)
