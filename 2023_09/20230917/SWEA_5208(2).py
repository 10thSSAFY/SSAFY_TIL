import sys
sys.stdin = open('res/input_SWEA_5208.txt', 'r')


def f(idx, cnt):
    global result
    if cnt >= result:
        return
    
    if idx >= N - 1:
        result = min(cnt, result)
        return

    for i in range(idx+lst[idx], idx, -1):
        f(i, cnt + 1)


T = int(input())
for tc in range(1, T+1):
    N, *lst = list(map(int, input().split()))
    result = 2147483647
    f(0, 0)
    result -= 1
    print(f'#{tc} {result}')
