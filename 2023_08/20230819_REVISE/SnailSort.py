import sys
sys.stdin = open('res/input_snail.txt', 'r')

'''
[입력]
9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
'''

lst = list(map(int, input().split()))
for _ in range(4):
    lst.extend(list(map(int, input().split())))
lst.sort()  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

N = 5
arr = [[0]*N for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0
r, c = 0, -1
for num in lst:
    newR, newC = r+dr[d], c+dc[d]
    if newR < 0 or newR >= N or newC < 0 or newC >= N or arr[newR][newC] != 0:
        d = (d+1)%4
    r, c = r+dr[d], c+dc[d]
    arr[r][c] = num

for a in arr:
    print(a)
