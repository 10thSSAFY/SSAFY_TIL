# 최적 경로
import sys
sys.stdin = open('res/input_1247.txt', 'r')

def f(lst, i, N):
    global min_result
    if i == N:
        my_sum = 0
        newLst = [0] + lst + [1]
        for l in range(N+1):
            my_sum += abs(x_lst[newLst[l]] - x_lst[newLst[l+1]])
            my_sum += abs(y_lst[newLst[l]] - y_lst[newLst[l+1]])
        if min_result > my_sum:
            min_result = my_sum
 
    else:
        for j in range(i, N):
            lst[i], lst[j] = lst[j] ,lst[i]
            f(lst, i+1, N)
            lst[i], lst[j] = lst[j] ,lst[i]
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
 
    x_lst = []
    y_lst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            x_lst.append(lst[i])
        else:
            y_lst.append(lst[i])
 
    idx = []
    for i in range(2, N+2):
        idx.append(i)
 
    min_result = 12345678910
    f(idx, 0, N)
 
    print(f'#{tc} {min_result}')
