# 그래프 경로
import sys
sys.stdin = open('res/input_4871.txt', 'r')

def path(Graph, Start, Goal):
    if Start == Goal:
        return 1
    visited = []
    stack = []
    stack.append(Start)
    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            stack.extend(Graph[tmp])
        if tmp == Goal:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)

    S, G = map(int, input().split())
    result = path(graph, S, G)

    print(f'#{tc} {result}')
