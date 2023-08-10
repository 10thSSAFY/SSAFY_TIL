# 쇠막대기 자르기
import sys
sys.stdin = open('res/input_5432.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    brackets = input().strip()
    brackets = list(brackets.replace('()', '|'))
    result = 0
    stack = []
    for i in brackets:
        if i == '|':
            result += len(stack)
        elif i == ')':
            result += 1
            stack.pop()
        elif i == '(':
            stack.append(i)
    
    print(f'#{tc} {result}')
