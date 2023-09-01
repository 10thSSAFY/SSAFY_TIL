# 그래프 경로
import sys
sys.stdin = open('res/input_4871.txt', 'r')

def has_path(graph, start, end, visited):
    if start == end:
        return 1
    
    visited[start] = True
    
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if has_path(graph, neighbor, end, visited):
                return 1
    
    return 0


T = int(input())

for case in range(1, T+1):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    
    S, E = map(int, input().split())
    
    visited = [False] * (V+1)
    
    result = has_path(graph, S, E, visited)
    print(f"#{case} {result}")
