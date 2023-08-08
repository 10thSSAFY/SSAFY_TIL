# 종이붙이기
import sys
sys.stdin = open('res/input_4869.txt', 'r')

def DP(N):
    if N == 0 or N == 1:
        return 1
    return DP(N-1) + 2*DP(N-2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N //= 10
    result = DP(N)
    print(f'#{tc} {result}')
