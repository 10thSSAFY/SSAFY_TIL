# 미로의 거리
import sys
sys.stdin = open('res/input_5105.txt', 'r')

def BFS(r, c, cnt):
    queue = [(r, c, cnt)]
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    while queue:
        vr, vc, cnt = queue.pop(0)
        if arr[vr][vc] == '3':
            return cnt-1
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newR, newC = vr + dr, vc + dc
            if 0 <= newR < N and 0 <= newC < N and arr[newR][newC] != '1':
                if not visited[newR][newC]:
                    cnt_up = cnt + 1
                    queue.append((newR, newC, cnt_up))
                    visited[newR][newC] = True
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
    result = BFS(R, C, 0)
    print(f'#{tc} {result}')
