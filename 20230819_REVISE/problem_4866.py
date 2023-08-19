# 괄호검사
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
import sys
sys.stdin = open('res/input_4866.txt', 'r')

pair = {'}': '{', ')': '('}

T = int(input())
for tc in range(1, T+1):
    lst = list(input().strip())
    stack = []
    result = 1
    for l in lst:
        if l in '({':
            stack.append(l)
        elif l in ')}':
            if not stack or pair[l] != stack.pop():
                result = 0
                break
    else:
        if stack:
            result = 0

    print(f'#{tc} {result}')
