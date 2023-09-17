import sys
sys.stdin = open('res/input_SWEA_5207.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    lst = list(map(int, input().split()))
    cnt = 0
    for num in lst:
        s, e = 0, N-1
        while s <= e:
            middle = (s + e) // 2
            value = A[middle]
            if value > num:
                e = middle - 1
            elif value < num:
                s = middle + 1
            else:
                cnt += 1
                break

    print(f"#{tc} {cnt}")
