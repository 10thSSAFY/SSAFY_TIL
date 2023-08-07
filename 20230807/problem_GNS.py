# GNS
import sys
sys.stdin = open('res/input_GNS.txt', 'r')

T = int(input())
orders = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(T):
    tc, N = map(str, input().split())
    N_list = list(map(str, input().split()))

    result = [0 for _ in range(int(N))]
    cnt = 0
    for order in orders:
        for Num in N_list:
            if order == Num:
                result[cnt] = Num
                cnt += 1

    print(tc)
    print(*result)
