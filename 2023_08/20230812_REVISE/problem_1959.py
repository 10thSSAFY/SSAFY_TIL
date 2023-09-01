import sys
sys.stdin = open('res/input_1959.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Nlist = list(map(int, input().split()))
    Mlist = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        Nlist, Mlist = Mlist, Nlist

    max_sum = 0
    for k in range(N):
        max_sum += Nlist[k] * Mlist[k]

    for i in range(M-N+1):
        my_sum = 0
        for j in range(N):
            my_sum += Nlist[j] * Mlist[j+i]
        if max_sum < my_sum:
            max_sum = my_sum

    print(f'#{tc} {max_sum}')
