# 파리퇴치 3
import sys
sys.stdin = open('res/input_12712.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for r in range(N):
        for c in range(N):
            score = arr[r][c]
            for l in range(1, M):
                for R, C in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0<=r+R*l<N and 0<=c+C*l<N:
                        score += arr[r+R*l][c+C*l]
            if result < score:
                result = score

            score = arr[r][c]
            for l in range(1, M):
                for R, C in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if 0<=r+R*l<N and 0<=c+C*l<N:
                        score += arr[r+R*l][c+C*l]
            if result < score:
                result = score
                
    print(f'#{tc} {result}')
