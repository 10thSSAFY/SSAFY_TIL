# 방 배정
import sys
sys.stdin = open('res/input_beakjoon_13300.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
info = [K-1] * 14
cnt = 0
for _ in range(N):
    S, Y = map(int, input().split())
    info[Y*2+S] += 1

for i in range(14):
    cnt += info[i]//K

print(cnt)
