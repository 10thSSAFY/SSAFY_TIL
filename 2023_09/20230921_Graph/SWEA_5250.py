# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용
import sys
sys.stdin = open('res/input_SWEA_5250.txt', 'r')

from collections import deque
 
def BFS(r, c):
    visited[r][c] = 0
    Q = deque()
    Q.append((r, c))
    while Q:
        r, c = Q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newR, newC = r + dr, c + dc
            if 0 <= newR < N and 0 <= newC < N:
                tmp = 0
                if arr[newR][newC] > arr[r][c]:
                    tmp = arr[newR][newC] - arr[r][c]
 
                new_visited = visited[r][c] + 1 + tmp
                if visited[newR][newC] > new_visited:
                    visited[newR][newC] = new_visited
                    Q.append((newR, newC))
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    visited = [[2147483647] * N for _ in range(N)]
    BFS(0, 0)
    result = visited[N-1][N-1]
    print(f'#{tc} {result}')
