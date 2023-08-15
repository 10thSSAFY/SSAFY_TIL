# 미로
import sys
sys.stdin = open('res/input_4875.txt', 'r')

def dfs(r, s):
    visited = [[False]*N for _ in range(N)]
    ST = [(r, s)]
    visited[r][s] = True
    while ST:
        vr, vc = ST.pop()
        if lst[vr][vc] == '3':
            return 1
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newR, newC = vr + dr, vc + dc
            if 0 <= newR < N and 0 <= newC < N and lst[newR][newC] != '1':
                if not visited[newR][newC]:
                    ST.append((newR, newC))
                    visited[newR][newC] = True
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if lst[r][c] == '2':
                break

    result = dfs(r, c)
    print(f'#{tc} {result}')
