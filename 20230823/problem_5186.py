# 이진수2
import sys
sys.stdin = open("res/input_5186.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    bi = float(1)
    result = ''
    for _ in range(12):
        bi /= 2
        if N >= bi:
            N -= bi
            result += '1'
        else:
            result += '0'
        if N == 0:
            break
    else:
        result = 'overflow'
    print(f'#{tc} {result}')