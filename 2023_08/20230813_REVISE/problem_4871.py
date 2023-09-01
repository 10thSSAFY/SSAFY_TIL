# 그래프 경로
import sys
sys.stdin = open('res/input_4871.txt', 'r')

def dfs(start, goal):
    stack = [start]
    visted = [False] * (V+1)
    visted[start] = True
    while stack:
        v = stack.pop()
        if v == goal:
            return 1
        for w in graph[v]:
            if not visted[w]:
                stack.append(w)
                visted[w] = True
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
    S, G = map(int, input().split())
    result = dfs(S, G)

    print(f'#{tc} {result}')
