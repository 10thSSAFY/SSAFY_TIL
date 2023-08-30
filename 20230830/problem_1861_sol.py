# 정사각형 방 (실행시간 개선)
import sys
sys.stdin = open('res/input_1861.txt', 'r')

def dfs(r, c, value):
    t = 0

    for dr, dc in [(), (), (), ()]:
        newR = r + dr
        newC = c + dc
        if 0 <= newR < N and 0 <= newC < N and value+1 == ARR[newR][newC]:
            t = dfs(newR, newC, ARR[newR][newC])
    
    return t+1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]