# 스도쿠 검증
import sys
sys.stdin = open('res/input_1974.txt', 'r')

def sudoku(arr):
    for i in range(9):
        cnt = [0]*10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:
                return 0

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

## 직접 구현하세요