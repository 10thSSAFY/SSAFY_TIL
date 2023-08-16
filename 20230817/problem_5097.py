# 회전
import sys
sys.stdin = open('res/input_5097.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    for _ in range(M):
        lst.append(lst.pop(0))

    resutl = lst[0]
    print(f'#{tc} {resutl}')
