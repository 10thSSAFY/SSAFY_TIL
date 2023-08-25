# 의석이의 세로로 말해요
import sys
sys.stdin = open('res/input_5356.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().strip()) for _ in range(5)]
    result = ''
    for c in range(15):
        for r in range(5):
            try:
                result += arr[r][c]
            except:
                pass

    print(f'#{tc} {result}')