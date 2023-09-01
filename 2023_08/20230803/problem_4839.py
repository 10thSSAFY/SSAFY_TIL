# 이진탐색
import sys
sys.stdin = open('input_4839.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    Al, Bl, Ar, Br = 1, 1, P, P

    while True:
        Ac = (Ar + Al) // 2
        Bc = (Br + Bl) // 2

        if Ac == A and Bc == B:
            result = 0
            break
        elif Ac == A:
            result = 'A'
            break
        elif Bc == B:
            result = 'B'
            break

        if Ac < A:
            Al = Ac
        else:
            Ar = Ac

        if Bc < B:
            Bl = Bc
        else:
            Br = Bc

    print(f'#{tc} {result}')
