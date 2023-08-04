# 달팽이 숫자
import sys
sys.stdin = open('input_1954.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    d = 0
    num = 1
    for i in range(N, 1, -2):
        r, c = d, d
        for j in range(i-1):
            arr[r][c] = num
            c += 1
            num += 1
        for j in range(i-1):
            arr[r][c] = num
            r += 1
            num += 1
        for j in range(i-1):
            arr[r][c] = num
            c -= 1
            num += 1
        for j in range(i-1):
            arr[r][c] = num
            r -= 1
            num += 1
        d += 1

    if N % 2 == 1:
        arr[d][d] = num

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
