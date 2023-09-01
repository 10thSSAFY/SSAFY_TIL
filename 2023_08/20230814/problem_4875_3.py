# 미로
import sys
sys.stdin = open('res/input_4875.txt', 'r')

def dfs(s, g):
    visited = [[False] * N for _ in range(N)]
    ST = [s]
    vr, vc = s
    visited[vr][vc] = True
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while ST:
        vr, vc = ST.pop()
        # for dr, dc in arr:
        if (vr, vc) == g:
            return 1
        for k in range(4):
            newR = vr + dr[k]
            newC = vc + dc[k]
            if 0 <= newR <N and 0 <= newC <N and arr[newR][newC] != '1' and not visited[newR][newC]:
                ST.append((newR, newC))
                visited[newR][newC] = True
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start = (i, j)
            elif arr[i][j] == '3':
                goal = (i, j)
    result = dfs(start, goal)
    print(f'#{tc} {result}')