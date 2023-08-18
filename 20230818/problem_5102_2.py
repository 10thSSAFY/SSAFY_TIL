# 노드의 거리
import sys
sys.stdin = open('res/input_5102.txt', 'r')

def BFS(start, goal):
    visted = [False] * (V+1)
    visted[start[0]] = True
    queue = [(start)]
    while queue:
        v, cnt = queue.pop(0)
        if v == goal:
            return cnt
        for w in graph[v]:
            if not visted[w]:
                cnt_up = cnt + 1
                queue.append((w, cnt_up))
                visted[w] = True
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
    result = BFS((S, 0), G)
    print(f'#{tc} {result}')
