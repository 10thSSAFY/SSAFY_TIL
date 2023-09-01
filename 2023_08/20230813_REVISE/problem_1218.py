# 괄호 짝짓기
import sys
sys.stdin = open('res/input_1218.txt', 'r')

pair = {')': '(', ']': '[', '}': '{', '>': '<'}

for tc in range(1, 11):
    N = int(input())
    data = input()

    stack = []
    result = 1
    for i in data:
        if i in '([{<':
            stack.append(i)
        elif stack and stack[-1] == pair[i]:
            stack.pop()
        else:
            result = 0
            break
    else:
        if len(stack) != 0:
            result = 0

    print(f'#{tc} {result}')
