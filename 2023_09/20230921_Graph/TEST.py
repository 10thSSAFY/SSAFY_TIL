import heapq

def prim(start):  # 정점 기준으로 내가 갈 수 있는 가장 짧은 곳
    heap = []
    # MST 에 포함되었는지 여부
    MST = [0] * V

    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))
    # 누적합 저장
    sum_weight = 0

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue

        # 방문 체크
        MST[v] = 1

        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        f, t, w = map(int, input().split())
        graph[f][t] = w
        graph[t][f] = w

    result = prim(0)
    print(f'#{tc} {result}')