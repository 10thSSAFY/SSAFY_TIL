# 특별한 정렬
import sys
sys.stdin = open('res/input_4843.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if lst[minIdx] > lst[j]:
                minIdx = j
        lst[minIdx], lst[i] = lst[i], lst[minIdx]

    result = [0 for _ in range(10)]
    for i in range(5):
        result[2*i] = lst[-1-i]
        result[2*i+1] = lst[i]

    print(f'#{tc}', *result)
