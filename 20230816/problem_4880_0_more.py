import sys
sys.stdin = open('res/input_4880.txt', 'r')

def winner(lst, start, end):
    if end == start:
        return lst[start]
    if end-start == 1:
        return lst[start]

    mid = (start + end) // 2
    winner1 = winner(lst, start, mid)
    winner2 = winner(lst, mid + 1, end)

    

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    students = [[lst[i], i] for i in range(N)]
    result = winner(students, 0, N - 1)
    print(f'#{tc} {result[1] + 1}')
