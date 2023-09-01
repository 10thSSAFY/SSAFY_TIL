# 설탕 배달
import sys
sys.stdin = open('res/input_beakjoon_2839.txt', 'r')

def bag():
    for i in range(N//5, -1, -1):
        tmp = N - 5*i
        for j in range(tmp//3, -1, -1):
            if tmp - j*3 == 0:
                return i+j
    else:
        return -1

N = int(input())
print(bag())
