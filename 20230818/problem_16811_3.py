# 당근 포장하기
import sys
sys.stdin = open('res/input_16811.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = sorted(map(int, input().split()))

    max_lst = lst[-1]
    cnt_lst = [0] * max_lst
    for l in lst:
        cnt_lst[l-1] += 1

    min_result = -1
    for i in range(1, max_lst):
        for j in range(i, max_lst):
            S, M, L = sum(cnt_lst[:i]), sum(cnt_lst[i:j]), sum(cnt_lst[j:])
            if 0 not in [S, M, L] and N//2 >= max(S, M, L):
                # print(cnt_lst[:i], cnt_lst[i:j], cnt_lst[j:])
                result = max(S, M, L) - min(S, M, L)
                if min_result == -1:
                    min_result = result
                else:
                    min_result = min(result, min_result)

    print(f"#{tc} {min_result}")
