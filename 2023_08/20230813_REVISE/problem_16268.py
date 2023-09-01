# 풍선팡 2
import sys
sys.stdin = open('res/input_16268.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(M):
            score = arr[r][c]
            for R, C in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0<=r+R<N and 0<=c+C<M:
                    score += arr[r+R][c+C]
            if result < score:
                result = score
                
    print(f'#{tc} {result}')
