T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    N_min = min(N_list)
    N_max = max(N_list)
    print(f'#{tc} {N_max - N_min}')
