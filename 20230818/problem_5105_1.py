# 미로의 거리 (스택으로 풀이, 현재 스택의 길이 만큼 pop(1)하면서 너비 우선 탐색)
import sys
sys.stdin = open('res/input_5105.txt', 'r')

def BFS(r, c):
    ST = [(r, c)]
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    cnt = 0
    while ST:
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
        cnt += 1
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
