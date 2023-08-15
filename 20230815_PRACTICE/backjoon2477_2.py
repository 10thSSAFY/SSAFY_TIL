# 참외밭
import sys
sys.stdin = open('res/input_backjoon2477.txt', 'r')

N = int(input())
dir = []
length = []
for _ in range(6):
    D, L = map(int, input().split())
    dir.append(D)
    length.append(L)

check = [0, 0, 0, 0, 0]
for idx in dir:
    check[idx] += 1

infos = [(3,1), (2,4)], [(1,4), (3,2)], [(2,3), (4,1)], [(4,2), (1,3)]

area = 0
for info in infos:
    if check[info[0][0]] == 1 and check[info[0][1]] == 1:
        for i in range(6):
            if (dir[i-1], dir[i]) == info[0]:
                area += length[i-1] * length[i]
            elif (dir[i-1], dir[i]) == info[1]:
                area -= length[i-1] * length[i]

print(area*N)
