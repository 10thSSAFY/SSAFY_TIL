# 직사각형
import sys
sys.stdin = open('res/input_beakjoon_2527.txt', 'r')

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    #print(x1, y1, p1, q1, x2, y2, p2, q2)
    if p2 < x1 or q2 < y1 or q1 < y2 or p1 < x2:
        print('d')
    elif (p1 == x2 or x1 == p2) and q1 == y2 or (p1 == x2 or x1 == p2) and y1 == q2:
        print('c')
    elif q1 == y2 or y1 == q2 or x1 == p2 or x2 == p1:
        print('b')
    else:
        print('a')
