# 창용 마을 무리의 개수
import sys
sys.stdin = open('res/input_SWEA_7465.txt', 'r')

def DFS(S):
    visited[S] = True
    stack = [S]
    while stack:
        n = stack.pop()
        for v in G[n]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        G[n1].append(n2)
        G[n2].append(n1)
    
    visited = [False] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            DFS(i)
    print(f'#{tc} {cnt}')
