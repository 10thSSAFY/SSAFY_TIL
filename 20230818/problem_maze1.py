# 미로1
import sys
sys.stdin = open('res/input_maze1.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(input().strip()) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    queue = [(1, 1)]
    visited[1][1] = True

    result = 0
    while queue:
        r, c = queue.pop(0)
        if arr[r][c] == '3':
            result = 1
            break
        for dr, dc in [(-1, 0), (1 ,0), (0, -1), (0, 1)]:
            if not visited[r+dr][c+dc] and arr[r+dr][c+dc] != '1':
                queue.append((r+dr, c+dc))
                visited[r+dr][c+dc] = True

    print(f'#{tc} {result}')
