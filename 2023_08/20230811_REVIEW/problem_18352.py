# 운동장에 파인 곳을 찾아주세요
import sys
sys.stdin = open('res/input_18352.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    depth = 100  # 운동장의 최대높이 + 1
    for r in range(1, N-1):
        for c in range(1, M-1):  # 테두리를 제외한 운동장 요소의 모든 높이 탐색
            h = arr[r][c]
            for d in range(4):
                # newR, newC = r+dr[d], c+dc[d]
                # if 0<=newR<N and 0<=newC<M:  # out of range 오류가 나지 않습니다.
                if h >= arr[r+dr[d]][c+dc[d]]:  # arr[r][c] 기준 상, 하, 좌, 우로 파임 조건이 틀리면
                    break
            else:  # 모든 상, 하, 좌, 우 파임 조건을 만족시키고 나면
                cnt += 1
                if depth > arr[r][c]:  # 가장 깊이 파인 곳의 높이
                    depth = arr[r][c] 
    
    if cnt == 0:  # 모든 구간 파악 후 파인 곳이 없으면
        depth = -1

    print(f'#{tc} {cnt} {depth}')
