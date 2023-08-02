# 전기버스
import sys
sys.stdin = open('input_4831.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())         # K = 3, N = 10, M = 5
    station = list(map(int, input().split()))   # station = [1, 3, 5, 7, 9]

    myPosition = 0
    cnt = 0

    while myPosition + K < N:
        temp = 0
        for pos in station:
            if myPosition + K >= pos:  
                temp = pos
            else:
                break
            
        if temp > myPosition:
            myPosition = temp
            cnt += 1
        else:
            cnt = 0
            break
                    
    print(f'#{tc} {cnt}')
