# 탈주범 검거
import sys
sys.stdin = open('res/input_1953.txt', 'r')

def f(depth, start):
    if depth == L:
        return

    Q = [start]
    while Q:
        vr, vc = Q.pop(0)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = vr + dr, vc + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                for ndr, ndc in way[arr[nr][nc]]:
                    if ndr+nr == vr and ndc+nc == vc:
                        visited[nr][nc] = 1
                        f(depth + 1, (nr, nc))
                        break

way = {1: [(1, 0), (-1, 0), (0, 1), (0, -1)], 2: [(-1, 0), (1, 0)], 3: [(0, -1), (0, 1)],
       4: [(-1, 0), (0, 1)], 5: [(1, 0), (0, 1)], 6: [(1, 0), (0, -1)], 7: [(-1, 0), (0, -1)]}

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    f(1, (R, C))

    result = 0
    for v in visited:
        result += sum(v)

    print(f'#{tc} {result}')