# 색종이 - 2
import sys
sys.stdin = open('res/input_beakjoon_2567.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = [[0] * 102 for _ in range(102)]
for _ in range(N):
    C, R = map(int, input().split())
    for k in range(10):
        arr[R+1+k][C+1:C+11] = [1] * 10

cnt = 0
for r in arr:
    temp = 0
    for i in r:
        if temp != i:
            temp = i
            cnt += 1

arr = [list(x) for x in zip(*arr)]
for r in arr:
    temp = 0
    for i in r:
        if temp != i:
            temp = i
            cnt += 1
print(cnt)
