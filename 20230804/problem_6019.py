# 기차 사이의 파리
import sys
sys.stdin = open('input_6019.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    time_sum = 0
    while D > 1e-7:
        time = D/(B+F)
        D -= (A+B) * time
        time_sum += time
        time = D/(A+F)
        D -= (A+B) * time
        time_sum += time

    result = time_sum * F
    print(f'#{tc} {result: .7f}')
