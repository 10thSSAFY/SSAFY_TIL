# 길찾기
import sys
sys.stdin = open('res/input_pathfind.txt', 'r')

for _ in range(10):
    tc, N = map(int, input().split())
    VE = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(N):
        graph[VE[i*2]].append(VE[i*2+1])
    
    Start, Goal = 0, 99

    visited = []
    stack = [Start]
    result = 0
    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            stack.extend(graph[tmp])
        if tmp == Goal:
            result = 1
            break
        
    print(f'#{tc} {result}')
