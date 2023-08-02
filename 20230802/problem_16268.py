# 풍선팡 2
import sys
sys.stdin = open('input_16268.txt', 'r')

T = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N, M = 5, 2
    arr = []
    for _ in range(N):
        line = list(map(int, input().split()))
        arr.append(line)
    
    scores = []
    for r in range(N):
        for c in range(M):
            score = arr[r][c]
            for d in range(4):
                newR = r + dr[d]
                newC = c + dc[d]
                if 0<= newR < N and 0 <= newC < M:
                    score += arr[newR][newC]
            scores.append(score)

    result = max(scores)
    print(f'#{tc} {result}')
