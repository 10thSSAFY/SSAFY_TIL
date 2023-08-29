# 물놀이를 가자
import sys
sys.stdin = open('res/input_10966.txt', 'r')
from collections import deque

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    BRD = [input() for _ in range(N)]
    DIS = [[0]*M for _ in range(N)]
    Q = deque()
    for i in range(N):
        for j in range(M):
            if BRD[i][j] == 'W':
                Q.append((j, i, 0))
    sumV = 0
    while Q:
        curX, curY, dis = Q.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            newX = curX+dx
            newY = curY+dy
            if 0 <= newX < M and 0 <= newY < N and BRD[newY][newX] == 'L':
                if DIS[newY][newX] == 0:
                    sumV += dis+1
                    DIS[newY][newX] = dis+1
                    Q.append((newX, newY, dis+1))

    print('#{} {}'.format(tc, sumV))