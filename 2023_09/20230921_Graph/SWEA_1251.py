# [S/W 문제해결 응용] 4일차 - 하나로
import sys
sys.stdin = open('res/input_SWEA_1251.txt', 'r')

import heapq

def prim(start):
    heap = []
    MST = [0] * N
    heapq.heappush(heap, (0, start))
    sum_weight = 0

    while heap:
        weight, v = heapq.heappop(heap)
        if MST[v]:
            continue
        MST[v] = 1
        sum_weight += weight
        for next in range(N):
            if G[v][next] == 0 or MST[next]:
                continue
            heapq.heappush(heap, (G[v][next], next))

    return sum_weight


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())
    G = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            weight = (x_lst[i] - x_lst[j]) ** 2 + (y_lst[i] - y_lst[j]) ** 2
            G[i][j] = weight
            G[j][i] = weight

    result = round(prim(0) * E)
    print(f'#{tc} {result}')
