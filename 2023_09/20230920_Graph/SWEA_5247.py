# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산
import sys
sys.stdin = open('res/input_SWEA_5247.txt', 'r')

from collections import deque

def BFS(V):
    queue = deque([V])
    while queue:
        num, cnt = queue.popleft()
        for newNum in [num+1, num-1, num*2, num-10]:
            if 1 <= newNum <= 1000000 and not visited[newNum]:
                visited[newNum] = True
                queue.append((newNum, cnt + 1))
                if newNum == M:
                    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [False] * 1000001
    visited[N] = True
    result = BFS((N, 1))
    print(f'#{tc} {result}')
