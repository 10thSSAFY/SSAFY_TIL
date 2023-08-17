# 파리퇴치3
import sys
sys.stdin = open('res/input_12712.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(N):
            score1 = score2 = arr[r][c]
            for d in range(1, M):
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newR, newC = r+dr*d, c+dc*d
                    if 0 <= newR < N and 0 <= newC < N:
                        score1 += arr[newR][newC]
            if result < score1:
                result = score1
            for d in range(1, M):
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    newR, newC = r+dr*d, c+dc*d
                    if 0 <= newR < N and 0 <= newC < N:
                        score2 += arr[newR][newC]
            if result < score2:
                result = score2

    print(f'#{tc} {result}')
