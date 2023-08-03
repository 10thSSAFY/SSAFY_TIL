import sys
sys.stdin = open('input_snail.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(5)]

sorted_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

snail = [[0] * N for _ in range(N)]

d = 0
idx = 0
for i in range(N,1,-2):
    r, c = d, d
    for _ in range(i-1):
        snail[r][c] = sorted_arr[idx]
        idx += 1
        c += 1
    for _ in range(i-1):
        snail[r][c] = sorted_arr[idx]
        idx += 1
        r += 1
    for _ in range(i-1):
        snail[r][c] = sorted_arr[idx]
        idx += 1
        c -= 1
    for _ in range(i-1):
        snail[r][c] = sorted_arr[idx]
        idx += 1
        r -= 1
    d += 1
snail[d][d] = sorted_arr[idx]
for k in snail:
    print(k)