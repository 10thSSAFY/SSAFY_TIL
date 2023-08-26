# 줄세우기
import sys
sys.stdin = open('res/input_beakjoon_10431.txt', 'r')

P = int(input())
for _ in range(P):
    T, *lst = map(int, input().split())
    line = [0]
    cnt = 0
    for i in range(len(lst)):
        for j in range(len(line), 0, -1):
            a, b = line[j-1], lst[i]
            if line[j-1] > lst[i]:
                cnt += 1
            else:
                line.insert(j, lst[i])
                break
    print(T, cnt)
