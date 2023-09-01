import sys
sys.stdin = open('res/input_1959.txt', 'r')

def BF(Nlist, Mlist):
    i = 0
    j = 0
    max_sum = -9999999999999
    my_sum = 0
    while i < N or j < M:
        if i == N:
            if max_sum < my_sum:
                max_sum = my_sum
            my_sum = 0
            j -= i-1
            i = 0
        my_sum += Nlist[i] * Mlist[j]
        i += 1
        j += 1
    if max_sum < my_sum:
        max_sum = my_sum
    return max_sum


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Nlist = list(map(int, input().split()))
    Mlist = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        Nlist, Mlist = Mlist, Nlist

    result = BF(Nlist, Mlist)
    print(f'#{tc} {result}')
