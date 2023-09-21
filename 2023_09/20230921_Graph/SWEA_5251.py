# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리
import sys
sys.stdin = open('res/input_SWEA_5251.txt', 'r')

import heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost  # dist: 누적거리, cost: 연결 엣지의 weight

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        f, t, w = map(int, input().split())
        graph[f].append([t, w])  # [f] = t, w
 
    distance = [2147483647] * (n+1)

    dijkstra(0)
    print(f'#{tc} {distance[-1]}')
