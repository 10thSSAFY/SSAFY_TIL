import sys
sys.stdin = open('res/input_SWEA_5208.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, *lst = list(map(int, input().split()))

    dp = [2147483647] * N
    dp[0] = -1
    for i in range(1, N):
        for j in range(i, min(i+lst[i-1], N)):
            dp[j] = min(dp[j], dp[i-1] + 1)
    
    result = dp[-1]
    print(f'#{tc} {result}')
