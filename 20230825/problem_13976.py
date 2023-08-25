# IM 대비 기지국
import sys
sys.stdin = open('res/input_13976.txt', 'r')

def charr(r, c, d):
    for l in range(1, d+1):
        for dr, dc in delta:
            newR, newC = r+dr*l, c+dc*l
            if 0 <= newR < N+1 and 0 <= newC < N:
                arr[newR][newC] = 'X'
 
delta = [(-1,0), (1,0), (0,-1), (0,1)]
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N+1)]
 
    for r in range(N+1):
        for c in range(N):
            if arr[r][c] == 'A':
                charr(r, c, 1)
            elif arr[r][c] == 'B':
                charr(r, c, 2)
            elif arr[r][c] == 'C':
                charr(r, c, 3)
            else:
                pass
    result = 0
    for line in arr:
        result += line.count('H')
    print(f'#{tc} {result}')