# 달팽이 숫자
import sys
sys.stdin = open('res/input_1954.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    r, c, d = 0, 0, 0
    for i in range(1, N*N+1):
        arr[r][c] = i
        newR, newC = r + dr[d], c + dc[d]
        if N <= newR or newR < 0 or N <= newC or newC < 0 or arr[newR][newC] != 0:
            d = (d+1) % 4
        r += dr[d]
        c += dc[d]


    print(f'#{tc}')
    for line in arr:
        print(*line)
