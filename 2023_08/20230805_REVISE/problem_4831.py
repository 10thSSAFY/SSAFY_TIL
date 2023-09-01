# 전기버스
import sys
sys.stdin = open('res/input_4831.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    now = 0
    cnt = 0
    while now < N - K:
        for i in range(now + K, now, -1):
            if i in lst:
                now = i
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')
