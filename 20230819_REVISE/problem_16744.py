# 마이쮸시뮬레이션_실습
import sys
sys.stdin = open('res/input_16744.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    P = 1
    N = int(input())
    queue = [(P, 1)]
    while N > 0:
        person, candy = queue.pop(0)
        N -= candy
        candy += 1
        queue.append((person, candy))
        P += 1
        queue.append((P, 1))

    print(f'#{tc} {person}')
