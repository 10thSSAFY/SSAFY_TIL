# 토너먼트 카드게임
import sys
sys.stdin = open('res/input_4880.txt', 'r')

def game(s, e):
    if s == e:
        return s
    M = (s+e)//2
    w1 = game(s, M)
    w2 = game(M+1, e)
    return winner(w1, w2)

def winner(w1, w2):
    if lst[w1] - lst[w2] == -1 or lst[w1] - lst[w2] == 2:
        return w2
    else:
        return w1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    result = game(1, N)
    print(f'#{tc} {result}')
