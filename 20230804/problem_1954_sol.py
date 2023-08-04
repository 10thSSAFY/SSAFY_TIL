# 달팽이 숫자
import sys
sys.stdin = open('input_1954.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    
    curR = 0
    curC = -1
    
    for value in range(1, N*N+1):
        newR, newC = curR + dr[d], curC + dc[d]
        
        if 0<=newR<N and 0<=newC<N and arr[newR][newC] == 0:
            curR += dr[d]
            curC += dc[d]
            arr[curR][curC] = value

        else:
            d = (d+1) % 4
            curR += dr[d]
            curC += dc[d]
            arr[curR][curC] = value

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
