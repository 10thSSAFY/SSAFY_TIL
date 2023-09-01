# 풍선팡 2
import sys
sys.stdin = open('input_16268.txt', 'r')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for r in range(N):
        for c in range(M):
            score = arr[r][c]
            for d in range(4):
                newR = r + dr[d]
                newC = c + dc[d]
                if 0<=newR<N and 0<=newC<M:
                    score += arr[newR][newC]
            if result < score:
                result = score
    
    print(f'#{tc} {result}')
