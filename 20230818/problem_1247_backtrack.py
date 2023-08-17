# 최적 경로
import sys
sys.stdin = open('res/input_1247.txt', 'r')

def backtrack(k, curSum, s_x, s_y):
    global min_result
    if curSum > min_result:
        return
    if k == N:
        curSum += abs(s_x - x_lst[1]) + abs(s_y - y_lst[1])
        if min_result > curSum:
            min_result = curSum
        return

    for i in range(2, N+2):
        if not used[i]:
            used[i] = True
            # arr[k] = i
            curSum += abs(s_x - x_lst[i]) + abs(s_y - y_lst[i])
            backtrack(k+1, curSum, x_lst[i], y_lst[i])
            curSum -= abs(s_x - x_lst[i]) + abs(s_y - y_lst[i])
            used[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    x_lst = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    y_lst = [lst[i] for i in range(len(lst)) if i % 2 != 0]

    min_result = sum(x_lst)+sum(y_lst)
    arr = [0] * N
    used = [True] * 2 + [False] * N
    backtrack(0, 0, x_lst[0], y_lst[0])
    print(f'#{tc} {min_result}')
