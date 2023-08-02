import sys
sys.stdin = open('4831.txt', 'r')

def check():
    # STOPS의 간격이 K보다 크면 결과가 0
    for st in range():
        if STOPS[st + 1] - STOPS[st] > K:
            return 0
        

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    STOPS = [0] + list(map(int, input().split())) + [N]

                    
    print(f'#{tc} {check()}')
