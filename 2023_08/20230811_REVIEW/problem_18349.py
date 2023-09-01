# 몇 개의 돌을 잡을 수 있을까요
import sys
sys.stdin = open('res/input_18349.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r, c = map(int, input().split())
    
    arr[r][c] = 1
    result = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for R in range(1, N-1):
        for C in range(1, N-1):
            if arr[R][C] == 2:
                for d in range(4):
                    # newR, newC = R+dr[d], C+dc[d]
                    # if 0<=newR<N and 0<=newC<N:  # out of range 오류가 나지 않습니다.
                    if arr[R+dr[d]][C+dc[d]] != 1:
                        break
                else:
                    result += 1

    print(f'#{tc} {result}')
