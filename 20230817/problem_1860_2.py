# 진기의 최고급 붕어빵
import sys
sys.stdin = open('res/input_1860.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    nums = sorted(list(map(int,input().split())))
    result = 'Possible'
    for s in range(len(nums)):
        if (nums[s]//M)*K - s - 1 < 0:
            result ='Impossible'
            break
    print(f'#{tc} {result}')
