# 롤케이크
import sys
sys.stdin = open('res/input_beakjoon_3985.txt', 'r')

L = int(input())  # 롤케이크 길이
N = int(input())  # 방청객 수
num1, res1, num2, res2 = 0, 0, 0, 0
Lcake = [0] * (L+1)
for i in range(1, N+1):
    P, K = map(int, input().split())
    if num1 < K-P+1:
        num1 = K-P+1
        res1 = i
    cnt = 0
    for j in range(P,K+1):
        if Lcake[j] == 0:
            Lcake[j] = i
            cnt += 1
    if num2 < cnt:
        num2 = cnt
        res2 = i

print(res1)
print(res2)
