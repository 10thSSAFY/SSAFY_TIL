# 보물상자 비밀번호
import sys
sys.stdin = open('res/input_5658.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    S = input()
    L = len(S) // 4  # 한번에 몇개의 숫자
    lst = []
    for idx in range(0, N, L):
        t = int(S[idx:idx+L], 16)
        lst.append(t)
    print(lst)
