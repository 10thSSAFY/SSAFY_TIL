# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리
import sys
sys.stdin = open('res/input_SWEA_5249.txt', 'r')


def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]
 
 
def union(x, y):
    x = find_set(x)
    y = find_set(y)
 
    if x == y:
        return
 
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
 
 
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x: x[2])
    parent = [i for i in range(V + 1)]
    weight = 0
    cnt = 0
 
    for i in range(E):
        if cnt == V:
            break
        n1, n2, w = edge[i]
        if find_set(n1) == find_set(n2):
            continue
        union(n1, n2)
        weight += w
 
    print(f'#{tc} {weight}')
