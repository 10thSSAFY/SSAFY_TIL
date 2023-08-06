# 부분집합의 합
import sys
sys.stdin = open('res/input_4837.txt', 'r')

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1<<12):
        partial_sum = 0
        cnt = 0
        for j in range(12):
            if i & (1<<j):
                partial_sum += lst[j]
                cnt += 1
        if cnt == N and partial_sum == K:
            result += 1
            
    print(f'#{tc} {result}')
