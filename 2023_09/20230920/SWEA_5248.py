# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
import sys
sys.stdin = open('res/input_SWEA_5248.txt', 'r')

from collections import deque

def BFS(num):
    queue = deque([num])
    visited[num] = True
    while queue:
        n = queue.popleft()
        for v in graph[n]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        s, e = lst[i * 2], lst[i * 2 + 1]
        graph[s].append(e)
        graph[e].append(s)

    visited = [False] * (N + 1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            BFS(i)

    print(f'#{tc} {cnt}')
