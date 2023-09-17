import sys
sys.stdin = open('res/input_SWEA_5209.txt', 'r')

def dfs(idx, currSum):
    global result

    if currSum >= result:
        return
    
    if idx == N:
        result = currSum

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(idx+1, currSum + V[idx][i])
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    result = 2147483647
    dfs(0, 0)

    print(f'#{tc} {result}')
