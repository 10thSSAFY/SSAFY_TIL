# 물놀이를 가자
import sys
sys.stdin = open('res/input_10966.txt', 'r')
    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]

    Queue = []
    water = []
    visited = [[100000]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W':
                Queue.append((r, c))
                visited[r][c] = 0

    depth = 0
    while Queue:
        depth += 1
        for _ in range(len(Queue)):
            vr, vc = Queue.pop(0)
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                newR, newC = vr+dr, vc+dc
                if 0 <= newR < N and 0 <= newC < M and visited[newR][newC] > depth:
                    Queue.append((newR, newC))
                    visited[newR][newC] = depth
        
    result = 0
    for v in visited:
        result += sum(v)

    print(f'#{tc} {result}')