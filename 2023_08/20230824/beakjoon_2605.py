import sys
sys.stdin = open('res/input_beakjoon_2605.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))
result = []
for i in range(N):
    if lst[i] == 0:
        result.append(i+1)
    else:
        result.insert(-lst[i], i+1)

print(*result)