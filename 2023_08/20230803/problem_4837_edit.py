# 부분집합의 합
import sys
sys.stdin = open('input_4837.txt', 'r')

T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1<<12):
        result_sum = 0
        result_cnt = 0
        for j in range(12):
            if i & (1<<j):
                result_sum += A[j]
                result_cnt += 1

        if result_sum == K and result_cnt == N:
            cnt += 1

    print(f'#{tc} {cnt}')
