# 노드의 거리
import sys
sys.stdin = open('res/input_5102.txt', 'r')

def BFS(start, goal):
    visted = [0] * (V+1)
    visted[start] = 0
    queue = [(start)]
    while queue:
        v= queue.pop(0)
        if v == goal:
            return visted[v]
        for w in graph[v]:
            if visted[w] == 0:
                queue.append((w))
                visted[w] = visted[v] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    S, G = map(int, input().split())
    result = BFS(S, G)
    print(f'#{tc} {result}')
