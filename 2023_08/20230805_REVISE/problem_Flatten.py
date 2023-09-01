# Flatten
import sys
sys.stdin = open('res/input_Flatten.txt', 'r')

def my_max(my_lst):
    max_num = my_lst[0]
    max_idx = 0
    for idx in range(len(my_lst)):
        if max_num < my_lst[idx]:
            max_num = my_lst[idx]
            max_idx = idx
    return max_num, max_idx


def my_min(my_lst):
    min_num = my_lst[0]
    min_idx = 0
    for idx in range(len(my_lst)):
        if min_num > my_lst[idx]:
            min_num = my_lst[idx]
            min_idx = idx
    return min_num, min_idx


for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    
    for _ in range(N):
        if my_max(lst)[0] - my_min(lst)[0] > 1:
            lst[my_max(lst)[1]], lst[my_min(lst)[1]] = my_max(lst)[0] - 1, my_min(lst)[0] + 1
        else:
            break

    result = my_max(lst)[0] - my_min(lst)[0]
    print(f'#{tc} {result}')
