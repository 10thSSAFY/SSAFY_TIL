# 경비원
import sys
sys.stdin = open('res/input_beakjoon_2564.txt', 'r')
input = sys.stdin.readline

C, R = map(int,input().split())
N = int(input())
store = []
for _ in range(N):
    d, w = map(int, input().split())
    store.append((d, w))

Dd, Dw = map(int, input().split())
result = 0
for Sd, Sw in store:
    if Dd == Sd:
        result += abs(Dw - Sw)
    elif Dd+Sd != 3 and Dd+Sd != 7:
        if Dd == 3:
            result += Sw
            if Sd == 1:
                result += Dw
            else:
                result += R-Dw
        elif Dd == 4:
            result += C-Sw
            if Sd == 1:
                result += Dw
            else:
                result += R-Dw
        elif Dd == 1:
            result += Sw
            if Sd == 3:
                result += Dw
            else:
                result += C-Dw
        elif Dd == 2:
            result += R-Sw
            if Sd == 3:
                result += Dw
            else:
                result += C-Dw
    else:
        if Dd == 1 or Dd == 2:
            result += R
            result += min(Dw+Sw, C-Dw+C-Sw)
        else:
            result += C
            result += min(Dw+Sw, C-Dw+C-Sw)

print(result)