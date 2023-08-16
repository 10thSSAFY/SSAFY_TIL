# 장훈이의 높은 선반
import sys
sys.stdin = open('res/input_1486.txt', 'r')

def partial(k):
    global minS
    if k == N:
        sumV = 0
        for i in range(N):
            if result_i[i]:
                sumV += lst[i]
        if B <= sumV < minS:
            minS = sumV
        return

    result_i[k] = 0
    partial(k + 1)

    result_i[k] = 1
    partial(k + 1)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    result_i = [-1] * N
    minS = sum(lst)
    partial(0)
    print(f'#{tc} {minS-B}')
