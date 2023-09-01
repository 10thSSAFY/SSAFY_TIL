# 5174 subtree
import sys
sys.stdin = open('res/input_5174.txt', 'r')

def res(node):
    global cnt
    if arr1[node] != 0:
        cnt += 1
        res(arr1[node])
    if arr2[node] != 0:
        cnt += 1
        res(arr2[node])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    V = E + 1
    arr1 = [0] * (V+1)
    arr2 = [0] * (V+1)
    for i in range(E):
        P, CH = lst[i*2], lst[i*2+1]
        if arr1[P] == 0:
            arr1[P] = CH
        else:
            arr2[P] = CH
    cnt = 1
    res(N)
    print(f'#{tc} {cnt}')
