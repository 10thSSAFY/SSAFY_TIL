# 홈 방범 서비스
import sys
sys.stdin = open('res/input_2117.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    result = 0
    for k in range(0, N + 1):
        vul = []
        for r in range(-k, k + 1):
            for c in range(-k, k + 1):
                if abs(r) + abs(c) <= k:
                    vul.append((r, c))
 
        for r in range(N):
            for c in range(N):
                cnt = 0
                for dr, dc in vul:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < N and 0 <= newC < N and arr[newR][newC] == 1:
                        cnt += 1
                if cnt*M - len(vul) >= 0 and result < cnt:
                    result = cnt
 
    print(f'#{tc} {result}')
