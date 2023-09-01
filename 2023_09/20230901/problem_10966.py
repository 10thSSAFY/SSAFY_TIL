# 물놀이를 가자
import sys
sys.stdin = open('res/input_10966.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    visited = [[10000000]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                visited[i][j] = 0
                continue
            if j != 0:
                visited[i][j] = min(visited[i][j-1]+1, visited[i][j])
            if i != 0:
                visited[i][j] = min(visited[i-1][j]+1, visited[i][j])

    cnt = 0
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 'W':
                visited[i][j] = 0
                continue
            if j != (M-1):
                visited[i][j] = min(visited[i][j+1]+1, visited[i][j])
            if i != (N-1):
                visited[i][j] = min(visited[i+1][j]+1, visited[i][j])
            
            cnt += visited[i][j]

    print(f'#{tc} {cnt}')