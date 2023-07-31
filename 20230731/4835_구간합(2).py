T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    s_lst = [0]
    tmp = 0

    for i in lst:
        tmp += i
        s_lst.append(tmp)

    result = []
    for i in range(N - M + 1):
        result.append(s_lst[M + i] - s_lst[i])

    print(f'#{tc} {max(result) - min(result)}')
