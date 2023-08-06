# 현주의 상자 바꾸기
import sys
sys.stdin = open('res/input_5789.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    lst = [0 for _ in range(N+1)]
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            lst[j] = i
        
    result = lst[1:]
    print(f'#{tc}', *result)
