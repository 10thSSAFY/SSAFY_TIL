# 풍선팡
import sys
sys.stdin = open('input_9490.txt', 'r')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        line = list(map(int, input().split()))
        arr.append(line)
    
    scores = []
    for i in range(N):
        for j in range(M):
            score = 0
            tmp = arr[i][j]
            score += tmp
            for t in range(1, tmp+1):
                for d in range(4):
                    newR = i + t*dr[d]
                    newC = j + t*dc[d]
                    if 0<=newR<N and 0<=newC<M:
                        score += arr[newR][newC]
            scores.append(score)
    
    result = max(scores)

    print(f'#{tc} {result}')