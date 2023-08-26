# 기상캐스터
import sys
sys.stdin = open('res/input_beakjoon_10709.txt', 'r')
input = sys.stdin.readline

H, W = map(int, input().split())
arr = [[-1]*W for _ in range(H)]
cloud = [list(input().strip()) for _ in range(H)]
for i in range(W):
    for r in range(H):
        for c in range(W):
            if cloud[r][c] == 'c' and arr[r][c] == -1:
                arr[r][c] = i
    for row in range(H):
        cloud[row].insert(0, '.')

for line in arr:
    print(*line)
