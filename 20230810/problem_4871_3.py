# 그래프 경로
import sys
sys.stdin = open('res/input_4871.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)

    S, G = map(int, input().split())
    visited = []
    stack=[S]
    result = 0
    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            stack.extend(graph[tmp])
        if tmp == G:
            result = 1
            break

    print(f'#{tc} {result}')
