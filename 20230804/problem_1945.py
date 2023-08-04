# 간단한 소인수분해
import sys
sys.stdin = open('input_1945.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = ''
    for i in [2, 3, 5, 7, 11]:
        cnt = 0
        while (N % i) == 0:
            N //= i
            cnt += 1
        result += str(cnt) + ' '

    print(f'#{tc} {result}')
