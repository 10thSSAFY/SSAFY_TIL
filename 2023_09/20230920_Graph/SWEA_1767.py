import sys
sys.stdin = open('res/input_SWEA_1767.txt', 'r')

def dfs(depth, cnt, connect):
    global result, max_connect

    if depth - connect > len_core - max_connect:
        return

    if depth == len_core:
        if connect > max_connect:
            max_connect = connect
            result = cnt
        elif connect == max_connect:
            result = min(cnt, result)
        return

    for k in range(depth, len_core):
        r, c = core[k]
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newR, newC = r, c
            tmp_set = []
            len_set = 0
            connect_success = False
            while True:
                newR, newC = newR + dr, newC + dc
                if newR < 0 or newR >= N or newC < 0 or newC >= N:
                    connect_success = True
                    break

                if arr[newR][newC] == 1:
                    break

                tmp_set.append((newR, newC))
                len_set += 1

            if connect_success:
                for tR, tC in tmp_set:
                    arr[tR][tC] = 1
                dfs(k + 1, cnt + len_set, connect + 1)
                for tR, tC in tmp_set:
                    arr[tR][tC] = 0
            dfs(k + 1, cnt, connect)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    core = []  # [(1, 2), (2, 5), (4, 1), (4, 3), (5, 1)]
    arr = []
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(1, N - 1):
            if i == 0 or i == N - 1:
                break
            if lst[j] == 1:
                core.append((i, j))
        arr.append(lst)
    len_core = len(core)

    visited = [[False] * N for _ in range(N)]
    result = 2147483647
    max_connect = 0

    dfs(0, 0, 0)

    print(f'#{tc} {result}')
