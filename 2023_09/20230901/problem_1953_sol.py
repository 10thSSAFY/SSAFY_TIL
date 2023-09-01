# 탈주범 검거
import sys
sys.stdin = open('res/input_1953.txt', 'r')

# 0:상, 1:하, 2:좌, 3:우
DELTA = [(-1,0), (1,0), (0,-1), (0,1)]
PIPE = [[0,0,0,0], [1,1,1,1], [1,1,0,0], [0,0,1,1],
        [1,0,0,1], [0,1,0,1], [0,1,1,0], [1,0,1,0]]
OPP = [1,0,3,2]


def bfs(r, c):
    visited = [[False] * M for _ in range(N)]
    Q = [(r, c, 1)]
    visited[r][c] = True
    while Q:
        r, c, t = Q.pop(0)
        if t == L:
            break
        for d in range(4):
            newR = r+DELTA[d][0]
            newC = c+DELTA[d][1]
            if 0 <= newR < N and 0 <= newC < M and not visited[newR][newC]:
                p1 = TUNNEL[r][c]
                p2 = TUNNEL[newR][newC]
                if PIPE[p1][d] and PIPE[p2][OPP[d]]:
                    Q.append((newR, newC, t+1))
                    visited[newR][newC] = True

    result = 0
    for rlst in visited:
