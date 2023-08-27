# 노드사이의 거리
import sys
sys.stdin = open('res/input_beakjoon_1240.txt', 'r')

input = sys.stdin.readline

def bfs(start):
    queue = []
    for tp in graph[start]:
        queue.append(tp)
    visited = [False] * (N+1)
    visited[start] = True
    while queue:
        n, d = queue.pop(0)
        if n == G:
            return d
        for nn, nd in graph[n]:
            if not visited[nn]:
                queue.append((nn, nd+d))
                visited[nn] = True


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2, d = map(int, input().split())
    graph[n1].append((n2, d))
    graph[n2].append((n1, d))

for _ in range(M):
    S, G = map(int, input().split())
    result = bfs(S)
    print(result)
