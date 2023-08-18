# 미로의 거리 (탐색한 경로의 깊이를 visited의 누적으로부터 추출)
import sys
sys.stdin = open('res/input_5105.txt', 'r')

def BFS(r, c):
    queue = [(r, c)]
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    while queue:
        vr, vc = queue.pop(0)
        if arr[vr][vc] == '3':
            return visited[vr][vc] - 2
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newR, newC = vr + dr, vc + dc
            if 0 <= newR < N and 0 <= newC < N and arr[newR][newC] != '1' and visited[newR][newC] == 0:
                if visited[newR][newC] == 0:
                    queue.append((newR, newC))
                    visited[newR][newC] = visited[vr][vc] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                R = i
                C = j
    result = BFS(R, C)
    print(f'#{tc} {result}')
