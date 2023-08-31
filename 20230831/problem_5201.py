# 컨테이너 운반
import sys
sys.stdin = open('res/input_5201.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Nlst = sorted(list(map(int, input().split())), reverse=True)
    Mlst = sorted(list(map(int, input().split())), reverse=True)

    result = 0
    for m in Mlst:
        for n in Nlst:
            if m >= n:
                result += n
                Nlst.remove(n)
                break

    print(f'#{tc} {result}')