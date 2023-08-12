# 풍선팡
import sys
sys.stdin = open('res/input_9490.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(M):
            my_sum = arr[r][c]
            for l in range(1, my_sum+1):
                for R, C in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0<=r+R*l<N and 0<=c+C*l<M:
                        my_sum += arr[r+R*l][c+C*l]
            if result < my_sum:
                result = my_sum
    print(f'#{tc} {result}')
