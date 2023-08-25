# 의석이의 세로로 말해요
import sys
sys.stdin = open('res/input_5356.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    rows = [list(input().strip()) for _ in range(5)]
    Max_len = 0
    for r in rows:
        Max_len = max(Max_len, len(r))
    for r in rows:
        for _ in range(Max_len - len(r)):
            r.append('')
    cols = [list(x) for x in zip(*rows)]

    result = ''
    for col in cols:
        result += ''.join(col)
    print(f'#{tc} {result}')
