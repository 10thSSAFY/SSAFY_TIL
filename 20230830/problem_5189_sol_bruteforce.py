# 전자카트
import sys
sys.stdin = open('res/input_5189.txt', 'r')

def perm(k):
    global result
    if k == N:
        sumV = 0
        for i in range(N-1):
            sp = bits[i]
            ep = bits[i+1]
            sumV += ARR[sp-1][ep-1]
        sumV += ARR[ep-1][0]
        if result > sumV:
            result = sumV
        # print(sumV)
        return
    
    for i in range(1, N+1):
        if not used[i]:
            bits[k] = i
            used[i] = True
            perm(k + 1)
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
    perm(1)
    print(f'#{tc} {result}')
