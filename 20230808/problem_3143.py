# 가장 빠른 문자열 타이핑
import sys
sys.stdin = open('res/input_3143.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())

    cnt = 0
    while B in A:
        A = A.replace(B,'', 1)
        cnt += 1
    cnt += len(A)

    print(f'#{tc} {cnt}')
