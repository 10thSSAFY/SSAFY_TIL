import sys
sys.stdin = open('res/input_maze2.txt', 'r')

def BFS(r, c):
    visited = [[False]*100 for _ in range(100)]
    visited[r][c] == True
    queue = [(r, c)]
    while queue:
        vr, vc = queue.pop(0)
        if arr[vr][vc] == 3:
            return 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newR, newC = vr+dr, vc+dc
            if arr[newR][newC] != 1 and not visited[newR][newC]:
                queue.append((newR, newC))
                visited[newR][newC] = True
    return 0

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().strip())) for _ in range(100)]
    result = BFS(1, 1)
    print(f'#{tc} {result}')