# 파리 퇴치
import sys
sys.stdin = open('input_2001.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            sum_result = 0
            for dr in range(M):
                for dc in range(M):
                    sum_result += arr[r+dr][c+dc]
            if result < sum_result:
                result = sum_result

    print(f'#{tc} {result}')
