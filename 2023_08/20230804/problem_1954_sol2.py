# 달팽이 숫자
import sys
sys.stdin = open('input_1954.txt', 'r')

T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    d = 0
    curR = curC = 0
    for value in range(1, N*N+1):
        arr[curR][curC] = value
        
        newR, newC = curR + dr[d], curC + dc[d]
        if newR<0 or newR>=N or newC<0 or newC>=N or arr[newR][newC] != 0: 
            d = (d+1) % 4

        curR += dr[d]
        curC += dc[d]

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
