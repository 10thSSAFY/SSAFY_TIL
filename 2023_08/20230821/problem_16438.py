# 16438 청소시키기
import sys
sys.stdin = open('res/input_16438.txt', 'r')

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())
for tc in range(1, T+1):
    N, M, K, R, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for _ in range(K):
        direct, dist = map(int, input().split())
        iwan = 1
        dr, dc = direction[direct]
        dust = arr[dr][dc]
        for i in range(dist):
            newR, newC = R+dr*iwan, C+dc*iwan
            if 0 <= newR < N and  0 <= newC < M:
                R, C = R+dr*iwan, C+dc*iwan
                dust += arr[R][C]
            else:
                iwan *= -1
                R, C = R+dr*iwan, C+dc*iwan
                dust += arr[R][C]

    print(f'#{tc} {dust} {R} {C}')