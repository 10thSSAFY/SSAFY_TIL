# 참외밭
import sys
sys.stdin = open('res/input_backjoon2477.txt', 'r')

N = int(input())
direction = []
length = []
for _ in range(6):
    D, L = map(int, input().split())
    direction.append(D)
    length.append(L)

check = [0, 0, 0, 0, 0]
for idx in direction:
    check[idx] += 1

area = 0
if check[1] == 1 and check[3] == 1:
    for i in range(6):
        if (direction[i-1], direction[i]) == (3,1):
            area += length[i-1] * length[i]
        elif (direction[i-1], direction[i]) == (2,4):
            area -= length[i-1] * length[i]
elif check[1] == 1 and check[4] == 1:
    for i in range(6):
        if (direction[i-1], direction[i]) == (1,4):
            area += length[i-1] * length[i]
        elif (direction[i-1], direction[i]) == (3,2):
            area -= length[i-1] * length[i]
elif check[2] == 1 and check[3] == 1:
    for i in range(6):
        if (direction[i-1], direction[i]) == (2,3):
            area += length[i-1] * length[i]
        elif (direction[i-1], direction[i]) == (4,1):
            area -= length[i-1] * length[i]
elif check[2] == 1 and check[4] == 1:
    for i in range(6):
        if (direction[i-1], direction[i]) == (4,2):
            area += length[i-1] * length[i]
        elif (direction[i-1], direction[i]) == (1,3):
            area -= length[i-1] * length[i]

print(area*N)
