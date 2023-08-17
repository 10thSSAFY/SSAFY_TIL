# 피자굽기
import sys
sys.stdin = open('res/input_5099.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    lst_i = [x for x in range(M)]
    ST = []
    for _ in range(N):
        ST.append(lst_i.pop(0))

    while ST:
        if len(ST) == 1:
            break
        else:
            lst[ST[0]] //= 2
            if lst[ST[0]] == 0:
                ST.pop(0)
                if lst_i:
                    ST.append(lst_i.pop(0))
                    lst[ST[-1]] //= 2
            else:
                ST.append(ST.pop(0))
                
    result = ST.pop() + 1
    print(f'#{tc} {result}')
