T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    total = numbers[:N]
    print(total)

    min_sum = total
    max_sum = total

    for i in range(N - M):
        total += numbers[M+i] - numbers[i]
        if total < min_sum:
            min_sum = total
        elif total > max_sum:
            max_sum = total

    print(f'#{tc} {max_sum - min_sum}')
