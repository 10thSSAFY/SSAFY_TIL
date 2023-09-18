import sys
sys.stdin = open('res/input_SWEA_5209.txt', 'r')

def f(k, currSum):
    global result
    if currSum >= result:
        return

    if k == N:
        result = currSum
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            f(k + 1, currSum + arr[k][i])
            used[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * N
    result = 2147483647
    f(0, 0)
    print(f'#{tc} {result}')
