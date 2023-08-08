# 초심자의 회문 검사
import sys
sys.stdin = open('res/input_1989.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    my_str = input()
    if my_str == my_str[::-1]:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
