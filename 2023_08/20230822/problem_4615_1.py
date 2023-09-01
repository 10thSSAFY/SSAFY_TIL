# 재미있는 오셀로 게임  10/30
import sys
sys.stdin = open('res/input_4615.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    I = N//2
    arr[I][I], arr[I-1][I], arr[I][I-1], arr[I-1][I-1] = 2, 1, 1, 2

    for _ in range(M):
        r, c, color = map(int, input().split())
        R, C = r-1, c-1
        stack = []
        arr[R][C] = color
        for dr, dc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            tmp = []
            for l in range(1, N+1):
                newR, newC = R + dr*l, C + dc*l
                if 0 <= newR < N and 0 <= newC < N:
                    if arr[newR][newC] == 0:
                        tmp = []
                        break
                    elif arr[newR][newC] != color:
                        tmp.append((newR, newC))
                    elif arr[newR][newC]:
                        stack.extend(tmp)
                        tmp = []
                        break
                else:
                    tmp = []
                    break
        

        for cr, cc in stack:
            arr[cr][cc] = color


    cnt1 = 0
    cnt2 = 0
    for a in arr:
        cnt1 += a.count(1)
        cnt2 += a.count(2)

    print(f'#{tc} {cnt1} {cnt2}')
