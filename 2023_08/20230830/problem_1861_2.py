# 정사각형 방 (실행시간 개선)
import sys
sys.stdin = open('res/input_1861.txt', 'r')

def dfs(R, C):
    global help
    global m, e
    queue = [(R,C)]
    depth = 1
    visited[R][C] = depth
    while queue:
        for _ in range(len(queue)):
            depth += 1
            vr, vc = queue.pop(0)
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                newR, newC = vr+dr, vc+dc
                if 0 <= newR < N and 0 <= newC < N and arr[vr][vc] + 1 == arr[newR][newC] and visited[newR][newC] < depth:
                    queue.append((newR, newC))
                    visited[newR][newC] = depth
 
        if help < depth:
            help = depth
            m, e = R, C
        elif help == depth and arr[m][e] > arr[R][C]:
            m, e = R, C

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]
 
    help = 0
    m, e = 0, 0
    for r in range(N):
        for c in range(N):
            dfs(r, c)
 
    print(f'#{tc} {arr[m][e]} {help-1}')
