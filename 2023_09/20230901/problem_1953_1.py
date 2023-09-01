# 탈주범 검거
import sys
sys.stdin = open('res/input_1953.txt', 'r')

def BFS(start):
    queue = [start]
    depth = 0
    while queue:
        depth += 1
        if depth == L:
            return
        for _ in range(len(queue)):
            vr, vc = queue.pop(0)
            delta = way[arr[vr][vc]]
            for dr, dc in delta:
                newR, newC = vr+dr, vc+dc
                if 0 <= newR < N and 0 <= newC < M and arr[newR][newC] != 0 and visited[newR][newC] == 0:
                    for newDr, newDc in way[arr[newR][newC]]:
                        if (newR+newDr, newC+newDc) == (vr, vc):
                            queue.append((newR, newC))
                            visited[newR][newC] = 1
                            break
  
way = {1:[(-1,0), (1,0), (0,-1), (0,1)], 2:[(-1,0), (1,0)], 3:[(0,-1), (0,1)],
       4:[(-1,0), (0,1)], 5:[(1,0), (0,1)], 6:[(1,0), (0,-1)], 7:[(-1,0), (0,-1)]}
  
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    BFS((R, C))
  
    result = 0
    for vst in visited:
        result += sum(vst)
  
    print(f'#{tc} {result}')