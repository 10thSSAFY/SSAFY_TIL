# 전기버스
import sys
sys.stdin = open('input_4831.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())         # K = 3, N = 10, M = 5
    station = list(map(int, input().split()))   # station = [1, 3, 5, 7, 9]
    station_idx = [0 for _ in range(N+1)]
    # station_idx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for idx in station:
        station_idx[idx] = 1
    # station_idx = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

    position_idx = 0
    cnt = 0
    while True:
        if position_idx + K + 1 > N:  # 종점까지 이동 가능한 포지션까지 왔을 경우에 종료
            break

        is_station = station_idx[position_idx : position_idx+1 + K] # is_station = [0, 1, 0, 1]
                                                                    # [{0, 1, 0, 1}, 0, 1, 0, 1, 0, 1, 0]
        temp = 0
        for i in range(K+1):
            if is_station[i] == 1:          # [{0, 1, 0, 1}, 0, 1, 0, 1, 0, 1, 0]
                temp = i                    # [{ , 1,  , 3}, 0, 1, 0, 1, 0, 1, 0] temp = 3

        if temp == 0:                       # [{0, 0, 0, 0}, 1, 1, 0, 1, 0, 1, 0]
            cnt = 0                         # 가능한 방법(cnt)= 0
            break

        position_idx += temp                # 가장 멀리 갈 수 있는 위치인 temp = 3 만큼 내 position 재설정
        cnt += 1                            # 충전소를 들린 횟수(cnt) +1 추가

    print(f'#{tc} {cnt}')