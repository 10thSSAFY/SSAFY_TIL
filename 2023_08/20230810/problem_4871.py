# 그래프 경로
import sys
sys.stdin = open('res/input_4871.txt', 'r')

def path(Start, Goal, Graph, Visited):
    if Start == Goal:
        return 1
    for tmp in Graph[Start]:
        if Visited[tmp] == 'F':
            Visited[tmp] = 'T'
            if path(tmp, Goal, Graph, Visited):
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = ['F'] * (V+1)
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)

    S, G = map(int, input().split())
    visited[S] = 'T'
    result = path(S, G, graph, visited)

    print(f'#{tc} {result}')
