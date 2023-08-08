# 괄호검사
import sys
sys.stdin = open('res/input_4866.txt', 'r')


pair = {')':'(','}':'{'}

T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    stack = []  # ???
    result = 1

    for i in lst:
        if i in '({':
            stack.append(i)

        elif i in ")}":
            if stack and pair[i] == stack[-1]:
                stack.pop()
            else:
                result = 0
                break

    if len(stack) != 0:
        result = 0

    print(f'#{tc} {result}')
