# 세포의 상태는
import sys
sys.stdin = open('res/input_18350.txt', 'r')

def stable(array, n, m):
    for r in range(n):
        for c in range(m):
            if array[r][c] == 1:
                for d in range(4):
                    newR, newC = r+dr[d], c+dc[d]
                    if 0<=newR<N and 0<=newC<M:
                        if arr[newR][newC] == 1:
                            return 0
    return 1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = stable(arr, N, M)

    print(f'#{tc} {result}')
