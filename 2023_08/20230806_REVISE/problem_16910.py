# 원 안의 점
import sys
sys.stdin = open('res/input_16910.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for r in range(1, N):
        for c in range(1, N):
            if r**2 + c**2 <= N**2:
                cnt += 1
    cnt *= 4
    cnt += N*4 + 1

    print(f'#{tc} {cnt}')
