import sys
sys.stdin = open('res/input_SWEA_5208.txt', 'r')


def f(k, cnt):
    global result
    if cnt >= result:
        return

    if k == N - 1:
        result = min(cnt, result)
        return

    for i in range(lst[k]):
        f(k+i + 1, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    N, *lst = list(map(int, input().split()))
    result = 2147483647
    f(0, -1)
    print(f'#{tc} {result}')
