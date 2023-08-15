# 토너먼트 카드게임
import sys
sys.stdin = open('res/input_4880.txt', 'r')

def winner(lst, start, end):
    if end == start:
        return lst[start]
    if end-start == 1:
        return lst[start]

    mid = (start + end) // 2
    winner1 = winner(lst, start, mid+1)
    winner2 = winner(lst, mid + 1, end)

    if (winner1[0] == 1 and winner2[0] == 3) or \
       (winner1[0] == 3 and winner2[0] == 1):
        return winner1
    elif (winner1[0] == 2 and winner2[0] == 1) or \
         (winner1[0] == 1 and winner2[0] == 2):
        return winner2
    else:
        return winner1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    students = [[lst[i], i] for i in range(N)]  # 각 학생의 카드와 인덱스를 묶음
    result = winner(students, 0, N - 1)
    print(f'#{tc} {result[1] + 1}')
