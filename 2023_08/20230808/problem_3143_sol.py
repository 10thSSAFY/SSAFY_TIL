# 가장 빠른 문자열 타이핑
import sys
sys.stdin = open('res/input_3143.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    t, p = input().split()

    N = len(t)
    M = len(p)

    tp = 0
    pp = 0
    cnt = 0
    while tp<N: #and pp<M:
        if t[tp] != p[pp]:
            tp = tp - pp
            pp = -1
        tp += 1
        pp += 1

        if pp == M:
            cnt += 1
            pp = 0

    print(f'#{tc} {N - M * cnt + cnt}')
