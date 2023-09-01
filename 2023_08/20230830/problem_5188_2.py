# 최소합
import sys
sys.stdin = open('res/input_5188.txt', 'r')

def go(start, curr_sum):
    global result
    if curr_sum > result:
        return
     
    if start == (N-1, N-1):
        result = min(result, curr_sum)
        return
 
    R, C = start
    if R+1 < N:
        go((R+1, C), curr_sum + arr[R+1][C])
    if C+1 < N:
        go((R, C+1), curr_sum + arr[R][C+1])
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    result = 2147483648
    go((0, 0), arr[0][0])
    print(f'#{tc} {result}')
