# 재미있는 오셀로 게임
import sys
sys.stdin = open('res/input_4615.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    BRD = [[0] * N for _ in range(N)]
    BRD[N // 2 - 1][N // 2 - 1] = 2
    BRD[N // 2][N // 2] = 2
    BRD[N // 2][N // 2 - 1] = 1
    BRD[N // 2 - 1][N // 2] = 1

    for turn in range(M):
        C, R, color = map(int, input().split())
        C -= 1
        R -= 1

        BRD[R][C] = color
        revers_c = 2 if color == 1 else 1

        for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            newR = R + dr
            newC = C + dc

            while 0<=newR<N and 0<=newC<N and BRD[newR][newC] == revers_c:
                newR += dr
                newC += dc

            if 0<=newR<N and 0<=newC<N and BRD[newR][newC] == color:
                while newR != R or newC != C:
                    newR -= dr
                    newC -= dc
                    BRD[newR][newC] = color

    cnt1 = 0
    cnt2 = 0
    for line in BRD:
        cnt1 += line.count(1)
        cnt2 += line.count(2)

    print(f'#{tc} {cnt1} {cnt2}')
