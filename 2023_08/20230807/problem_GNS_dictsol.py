# GNS
import sys
sys.stdin = open('res/input_GNS.txt', 'r')

T = int(input())
for _ in range(T):
    tc, N = map(str, input().split())
    lst = list(map(str, input().split()))
    magic_dict = {"ZRO": 0,
                  "ONE": 0,
                  "TWO": 0,
                  "THR": 0,
                  "FOR": 0,
                  "FIV": 0,
                  "SIX": 0,
                  "SVN": 0,
                  "EGT": 0,
                  "NIN": 0}
    
    for num in lst:
        magic_dict[num] += 1

    result = [0 for _ in range(int(N))]
    idx = 0
    for my_key, my_value in magic_dict.items():
        for i in range(my_value):
            result[idx] = my_key
            idx += 1
            
    print(tc)
    print(*result)
