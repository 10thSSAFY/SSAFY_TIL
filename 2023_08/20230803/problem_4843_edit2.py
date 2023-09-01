# 특별한 정렬
import sys
sys.stdin = open('input_4843.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    result = ''
    for c in range(5):
        for i in range(0, c+1):
            curIdx = 0
            for j in range(1, N-i):
                if lst[curIdx] < lst[j]:
                    curIdx = j

            lst[curIdx], lst[N-i-1] = lst[N-i-1], lst[curIdx]

        result += ' '+str(lst[-1-c])

        for i in range(0, c+1):
            curIdx = 0
            for j in range(1, N-i):
                if lst[curIdx] > lst[j]:
                    curIdx = j

            lst[curIdx], lst[N - i - 1] = lst[N - i - 1], lst[curIdx]

        result += ' '+str(lst[-1-c])

    print(f'#{tc}{result}')
