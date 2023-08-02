# 어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open('input_1979.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for r in range(N):
        arr_sum = 0
        for c in range(N):
            if arr[r][c] == 1:
                arr_sum += 1
            elif arr[r][c] == 0:
                if arr_sum == M:
                    cnt += 1
                arr_sum = 0
        if arr_sum == M:
            cnt += 1

    for r in range(N):
        arr_sum = 0
        for c in range(N):
            if arr[c][r] == 1:
                arr_sum += 1
            elif arr[c][r] == 0:
                if arr_sum == M:
                    cnt += 1
                arr_sum = 0
        if arr_sum == M:
            cnt += 1

    print(f'#{tc} {cnt}')
