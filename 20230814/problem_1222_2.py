# 계산기 1
import sys
sys.stdin = open('res/input_1222.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    string = input().strip()
    nums = ''
    plus = ''
    for i in string:
        if i == '+':
            plus += i
        elif i:
            nums += i
    new_string = nums + plus
    stack = []
    for j in new_string:
        if j == '+':
            stack.append(stack.pop()+stack.pop())
        else:
            stack.append(int(j))
    result = stack[0]
    print(f'#{tc} {result}')
