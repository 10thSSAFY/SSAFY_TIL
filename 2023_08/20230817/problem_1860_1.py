# 진기의 최고급 붕어빵
import sys
sys.stdin = open('res/input_1860.txt', 'r')

def how(M, K, peoples):
    sec = 0
    KWBS = 0
    while peoples:
        if sec != 0 and sec % M == 0:
            KWBS += K
        while sec in peoples:
            peoples.pop(0)
            if KWBS > 0:
                KWBS -= 1
            else:
                return 'Impossible'
        sec += 1
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    peoples = sorted(list(map(int, input().split())))
    result = how(M, K, peoples)
    print(f'#{tc} {result}')
