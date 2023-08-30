# 전자카트
import sys
sys.stdin = open('res/input_5189.txt', 'r')

def perm(k, sumV):
    global result
    if result < sumV:
        return
    if k == N:
        ep = bits[-1]
        sumV += ARR[ep-1][0]
        if result > sumV:
            result = sumV
        return
    
    for i in range(1, N+1):
        if not used[i]:
            bits[k] = i
            used[i] = True
            sp = bits[k-1]
            ep = bits[k]
            perm(k + 1, sumV + ARR[bits[k-1]-1][i-1])
            used[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    result = 100*10
    bits = [-1] * N
    used = [False] * (N+1)
    bits[0] = 1
    used[1] = True
    perm(1, 0)
    print(f'#{tc} {result}')
