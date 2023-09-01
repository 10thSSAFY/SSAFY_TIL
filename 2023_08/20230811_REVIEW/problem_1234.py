# [S/W 문제해결 기본] 10일차 - 비밀번호
import sys
sys.stdin = open('res/input_1234.txt', 'r')

for tc in range(1, 11):
    N, PW = input().strip().split()
    stack = []
    for num in PW:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)
    result = ''.join(stack)

    print(f'#{tc} {result}')
