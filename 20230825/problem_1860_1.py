# 진기의 최고급 붕어빵
import sys
sys.stdin = open('res/input_1860.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # N 손님수, M초마다, K개 생산
    arr = sorted(list(map(int, input().split())))  # N 명이 각각 도착하는 시간
    
    result = 'Possible'
    for i in range(N):
        if (arr[i] // M) * K - (i+1) < 0:
            result = 'Impossible'
            break
    
    print(f'#{tc} {result}')
