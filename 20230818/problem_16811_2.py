# 당근 포장하기
import sys
sys.stdin = open('res/input_16811.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    cnt_lst = [0] * (max(lst)+1)
    for l in lst:
        cnt_lst[l] += 1
    cnt_lst.pop(0)

    min_result = -1
    for i in range(1, N+1):
        for j in range(i, N+1):
            S, M, L = sum(cnt_lst[:i]), sum(cnt_lst[i:j]), sum(cnt_lst[j:])
            if S != 0 and L != 0 and M != 0:
                if N//2 >= S and N//2 >= M and N//2 >= L:
                    if min_result > max(S,M,L) - min(S,M,L) or min_result == -1:
                        min_result = max(S,M,L) - min(S,M,L)

    print(f'#{tc} {min_result}')