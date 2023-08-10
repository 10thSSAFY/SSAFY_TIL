# 두 개의 숫자열
import sys
sys.stdin = open('res/input_1959.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Nlst = list(map(int, input().split()))
    Mlst = list(map(int, input().split()))
 
    if N > M:  
        N, M = M, N
        Nlst, Mlst = Mlst, Nlst
 
    result = 0
    for i in range(M-N+1):
        sumV = 0
        for j in range(N):
            sumV += Nlst[j] * Mlst[i+j]
        if result <= sumV:
            result = sumV
 
    print(f'#{t} {result}')
