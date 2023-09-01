# 비밀번호
import sys
sys.stdin = open('res/input_password.txt', 'r')

for tc in range(1, 11):
    N, pw = input().strip().split()
    stack = []
    for i in pw:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    result = ''.join(stack)

    print(f'#{tc} {result}')
