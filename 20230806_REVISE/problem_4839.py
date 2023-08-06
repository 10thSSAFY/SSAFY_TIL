# 이진탐색
import sys
sys.stdin = open('res/input_4839.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    la, ra, lb, rb = 1, P, 1, P
    while True:
        Ca = int((la+ra)/2)
        Cb = int((lb+rb)/2)
        if Ca == A and Cb == B:
            result = 0
            break
        elif Ca == A:
            result = "A"
            break
        elif Cb == B:
            result = "B"
            break
        
        if Ca > A:
            ra = Ca
        else:
            la = Ca

        if Cb > B:
            rb = Cb
        else:
            lb = Cb

    print(f'#{tc} {result}')
