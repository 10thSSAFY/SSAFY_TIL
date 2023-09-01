# 최대 상금
import sys
sys.stdin = open('res/input_1244.txt', 'r')

def go(lst):
    tmp = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            tmp.append(int(''.join(lst)))
            lst[i], lst[j] = lst[j], lst[i]

    tmp = max(tmp)
    tmp = str(tmp)
    tmp_lst = []
    for t in tmp:
        tmp_lst.append(t)
    return tmp_lst


T = int(input())
for tc in range(1, T + 1):
    lst, N = input().split()
    N = int(N)
    lst = list(lst)
    for _ in range(N):
        lst = go(lst)

    print(f'#{tc} {"".join(lst)}')