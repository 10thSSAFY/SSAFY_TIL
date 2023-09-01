# 쇠막대기 자르기
import sys
sys.stdin = open('res/input_5432.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    lst = input()

    stack = []
    result = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            stack.append(i)
        elif stack[-1] == i - 1:
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

    print(f'#{tc} {result}')
