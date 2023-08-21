# 5174 subtree
import sys
sys.stdin = open('res/input_5174.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr =  list(map(int, input().split()))
    graph = [[] for _ in range(E+2)]
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        graph[p].append(c)
    cnt = 0

    S = [N]
    cnt = 0
    while S:
        v = S.pop()
        cnt += 1
        for w in graph[v]:
            S.append(w)

    print(f'#{tc} {cnt}')
