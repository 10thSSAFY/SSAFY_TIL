# [S/W 문제해결 응용] 4일차 - 보급로
import sys
sys.stdin = open('res/input_SWEA_1249.txt', 'r')

from collections import deque
 
def BFS(r, c):
    Queue = deque()
    Queue.append((r, c))
    while Queue:
        r, c = Queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newR, newC = r+dr, c+dc
            if 0 <= newR < N and 0 <= newC < N:
                tmp = 0
                if arr[newR][newC] > 0:
                    tmp = arr[newR][newC]
 
                new_visited = visited[r][c] + tmp
                if visited[newR][newC] > new_visited:
                    visited[newR][newC] = new_visited
                    Queue.append((newR, newC))
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[2147483647] * N for _ in range(N)]
    visited[0][0] = 0
    BFS(0, 0)
    result = visited[N-1][N-1]
    print(f'#{tc} {result}')
