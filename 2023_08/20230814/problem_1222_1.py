# 계산기 1
import sys
sys.stdin = open('res/input_1222.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    lst = list(input())
    stack = []
    for i in lst:
        if i != '+':
            if stack:
                stack.append(int(i)+stack.pop())
            else:
                stack.append(int(i))
    result = stack[0]
    print(f'#{tc} {result}')
