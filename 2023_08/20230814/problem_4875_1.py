# 미로
import sys
sys.stdin = open('res/input_4875.txt', 'r')

def dfs(start, goal):
    stack = [start]
    vr, vc = start
    visited[vr][vc] = True
    while stack:
        vr, vc = stack.pop()
        if (vr, vc) == goal:
            return 1
        for wr, wc in graph[vr][vc]:
            if not visited[wr][wc]:
                stack.append((wr, wc))
                visited[wr][wc] = True
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == '2':
                S = (r, c)
            elif arr[r][c] == '3':
                G = (r, c)

    graph = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] != '1':
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= r+dr < N and 0 <= c+dc < N:
                        if arr[r+dr][c+dc] != '1':
                            graph[r][c].append((r+dr, c+dc))
    visited = [[False] * N for _ in range(N)]
    result = dfs(S, G)
    print(f'#{tc} {result}')
