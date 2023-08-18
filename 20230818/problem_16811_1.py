# 당근 포장하기 (실행 시간 초과)
import sys
sys.stdin = open('res/input_16811.txt', 'r')

def balance(Slst, Mlst, Llst):
    for s in Slst:
        if s in Mlst or s in Llst:
            return 0
    for m in Mlst:
        if m in Llst:
            return 0
    return 1

def boxing(lst):
    min_dif = 10000000
    for i in range(1, N):
        for j in range(i+1, N):
            S, M, L = lst[:i], lst[i:j], lst[j:]
            if balance(S, M, L) and len(S) <= N//2 and len(M) <= N//2 and len(L) <= N//2:
                D = max(len(S), len(M), len(L)) - min(len(S), len(M), len(L))
                if min_dif > D:
                    min_dif = D
    if min_dif == 10000000:
        return -1
    else:
        return min_dif

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    result = boxing(lst)
    print(f'#{tc} {result}')
