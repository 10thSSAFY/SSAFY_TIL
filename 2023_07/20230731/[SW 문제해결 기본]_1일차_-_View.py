T = 10
for tc in range(1, T+1):
    N = int(input())
    high = list(map(int, input().split()))
    total = 0
    for i in range(2, N-2):
        view = min([high[i] - high[i-2], high[i] - high[i-1], high[i] - high[i+1], high[i] - high[i+2]])
        if view > 0:
            total += view

    print(f'#{tc} {total}')
