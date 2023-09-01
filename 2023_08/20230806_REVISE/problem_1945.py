# 간단한 소인수분해
import sys
sys.stdin = open('res/input_1945.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0 for _ in range(5)]
    prims = [2, 3, 5, 7, 11]
    for i in range(5):
        cnt = 0
        while N % prims[i] == 0:
            N //= prims[i]
            cnt += 1
        arr[i] = cnt

    print(f'#{tc}', *arr)
