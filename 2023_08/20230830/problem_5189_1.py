# 전자카트
import sys
sys.stdin = open('res/input_5189.txt', 'r')

def check(way):
    global result
    cur_sum = 0
    for i in range(len(way)-1):
        cur_sum += arr[way[i]-1][way[i+1]-1]
        if cur_sum > result:
            return
    result = min(result, cur_sum)
 
 
def permute(k):
    if k == N-1:
        check(p)
        return
    for i in range(N-1):
        if not used[i]:
            used[i] = True
            p[k+1] = lst[i]
            permute(k+1)
            used[i] = False
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [x for x in range(2, N+1)]
 
    used = [False] * (N-1)
    p = [1] * (N+1)
    result = 2147483648
    permute(0)
    print(f'#{tc} {result}')