# 현주의 상자 바꾸기
import sys
sys.stdin = open('input_5789.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0 for _ in range(N+1)]
    for num in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            arr[i] = num

    result = arr[1:]
    print(f'#{tc}', *result)
