# 노드의 거리
import sys
sys.stdin = open('res/input_5102.txt', 'r')

def BFS(start, goal):
    visted = [False] * (V+1)
    visted[start] = True
    ST = [start]
    cnt = 0
    while ST:
        for _ in range(len(ST)):
            v = ST.pop(0)
            if v == goal:
                return cnt
            for w in graph[v]:
                if not visted[w]:
                    ST.append(w)
                    visted[w] = True
        cnt += 1
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
