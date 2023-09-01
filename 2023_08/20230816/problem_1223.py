# 계산기
import sys
sys.stdin = open('res/input_1223.txt', 'r')

def cal(v1, v2, op):
    if op == '+':
        return v2 + v1
    elif op == '*':
        return v2 * v1

icp = {'+': 1, '*': 2}

for tc in range(1, 11):
    N = int(input())
    infix = input()

    postfix = ''
    stack = []
    for i in infix:
        if i.isdigit():
            postfix += i
        else:
            while stack and icp[stack[-1]] >= icp[i]:
                v = stack.pop()
                postfix += v
            stack.append(i)
    while stack:
        v = stack.pop()
        postfix += v

    stack = []
    for i in postfix:
        if i.isdigit():
            stack.append(i)
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(cal(int(v1), int(v2), i))

    result = stack.pop()
    print(f'#{tc} {result}')
