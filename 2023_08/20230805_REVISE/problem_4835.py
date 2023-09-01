# 구간합
import sys
sys.stdin = open('res/input_4835.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    interval_sum = 0
    for i in range(M):
        interval_sum += lst[i]

    max_sum = min_sum = interval_sum
    for j in range(N-M):
        interval_sum += lst[j+M] - lst[j]
        if max_sum < interval_sum:
            max_sum = interval_sum
        if min_sum > interval_sum:
            min_sum = interval_sum      
    result = max_sum - min_sum

    print(f'#{tc} {result}')
