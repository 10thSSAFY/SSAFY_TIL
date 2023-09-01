# 풍선팡2
import sys
sys.stdin = open('res/input_16268.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    for r in range(N):
        for c in range(M):
            score = lst[r][c]
            for d in range(4):
                if 0 <= r+dr[d] < N and 0 <= c+dc[d] < M:
                    score += lst[r+dr[d]][c+dc[d]]
            if max_score < score:
                max_score = score
    
    print(f'#{tc} {max_score}')
