# 5178 노드의 합
import sys
sys.stdin = open('res/input_5178.txt', 'r')

T = int(input())
for case in range(1, T + 1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N + 1)

    for _ in range(M):
        leaf, value = map(int, input().split())
        nodes[leaf] = value

    for i in range(N, 1, -1):
        parent = i // 2
        nodes[parent] += nodes[i]
    result = nodes[L]

    print(f"#{case} {result}")
