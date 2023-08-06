# 풍선팡
import sys
sys.stdin = open('res/input_9490.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(M):
            score = arr[r][c]
            for i in range(1, score+1):
                for d in range(4):
                    if 0 <= r + dr[d]*i < N and 0 <= c + dc[d]*i < M:
                        score += arr[r + dr[d]*i][c + dc[d]*i]
            if result < score:
                result = score
    
    print(f'#{tc} {result}')
