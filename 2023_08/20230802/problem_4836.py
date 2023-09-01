# 색칠하기
import sys
sys.stdin = open('input_4836.txt', 'r')

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    red = []
    blue = []

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if color == 1 and (r,c) not in red:
                    red.append((r,c))
                elif color == 2 and (r,c) not in blue:
                    blue.append((r,c))
                    
    result = len( set(red) & set(blue) )
    
    print(f'#{tc} {result}')
