# 미로의 거리
import sys
sys.stdin = open('res/input_5105.txt', 'r')

def BFS(r, c):
    ST = [(r, c)]
    visited[r][c] = True
    cnt = -1
    while ST:
        cnt += 1
        # print(ST, cnt)
        for _ in range(len(ST)):
            vr, vc = ST.pop(0)
            if arr[vr][vc] == '3':
                return cnt-1
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newR, newC = vr + dr, vc + dc
                if 0 <= newR < N and 0 <= newC < N and arr[newR][newC] != '1':
                    if not visited[newR][newC]:
                        ST.append((newR, newC))
                        visited[newR][newC] = True
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '2':
                break
    visited = [[False] * N for _ in range(N)]
    result = BFS(r, c)
    print(f'#{tc} {result}')
