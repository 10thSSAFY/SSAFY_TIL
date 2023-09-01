# 도로와 신호등
import sys
sys.stdin = open('res/input_beakjoon_2980.txt', 'r')
input = sys.stdin.readline

N, L = map(int, input().split())
sign = dict()
for _ in range(N):
    D, R, G = map(int, input().split())
    sign[D] = [R, G]

sec = 0
pos = 1
while pos < L:
    if pos not in sign:
        sec += 1
        pos += 1
    else:
        tmp = sec % (sign[pos][0] + sign[pos][1])
        if tmp < sign[pos][0]:
            sec += 1
        else:
            sec += 1
            pos += 1

print(sec)
