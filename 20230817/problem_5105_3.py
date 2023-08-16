# 미로의 거리
import sys
sys.stdin = open('res/input_5105.txt', 'r')

def BFS(r, c):
    ST = [(r, c)]
    visited[r][c] = True
    distance[r][c] = 0  # 시작 위치의 거리는 0
    
    while ST:
        vr, vc = ST.pop(0)
        
        if arr[vr][vc] == '3':
            return distance[vr][vc] - 1
            
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newR, newC = vr + dr, vc + dc
            if 0 <= newR < N and 0 <= newC < N and arr[newR][newC] != '1':
                if not visited[newR][newC]:
                    ST.append((newR, newC))
                    visited[newR][newC] = True
                    distance[newR][newC] = distance[vr][vc] + 1  # 새로운 위치의 거리를 갱신
                    
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '2':
                break
    visited = [[False] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]  # 각 위치까지의 거리 정보를 저장하는 리스트
    result = BFS(r, c)
    print(f'#{tc} {result}')

