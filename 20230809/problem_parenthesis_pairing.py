# 비밀번호
import sys
sys.stdin = open('res/input_parenthesis_pairing.txt', 'r')

pair = {')': '(', ']': '[', '}': '{', '>': '<'}

for tc in range(1, 11):
    N = int(input())
    string = list(input().strip())
    stack = []
    result = 1
    for chr in string:
        if chr in '([{<':
            stack.append(chr)
        elif stack and stack[-1] == pair[chr]:
            stack.pop()
        else:
            result = 0
    else:
        if stack:
            result = 0

    print(f'#{tc} {result}')
