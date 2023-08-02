# Flatten
import sys
sys.stdin = open('input_Flatten.txt', 'r')

T = 10
for tc in range(1, T+1):
    chance = int(input())
    data = list(map(int, input().split()))

    while chance > 0:
        data[data.index(max(data))] = max(data) - 1
        data[data.index(min(data))] = min(data) + 1
        chance -= 1

    print(f'#{tc} {max(data) - min(data)}')