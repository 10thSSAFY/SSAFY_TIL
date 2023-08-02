# 부분집합의 합
import sys
sys.stdin = open('input_4837.txt', 'r')

T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
len_A = len(A)

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1<<len_A):
        line = []
        for j in range(len_A):
            if i & (1<<j):
                line.append(A[j])

        if sum(line) == K and len(line) == N:
            # print('line =', line)
            cnt += 1

    print(f'#{tc} {cnt}')
