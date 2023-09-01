# 파리 퇴치
import sys
sys.stdin = open('res/input_2001.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            score = 0
            for k in range(M):
                for l in range(M):
                    score += arr[i+k][j+l]
            if result < score:
                result = score

    print(f'#{tc} {result}')
