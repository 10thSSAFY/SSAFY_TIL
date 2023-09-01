# 베이비진 게임
import sys
sys.stdin = open('res/input_5203.txt', 'r')

# 베이비진이면 True/ False
def isBabygin(cnts):
    for i in range(10):
        if cnts[i] >= 3:
            return True
        if cnts[i] >= 1 and cnts[i+1] >= 1 and cnts[i+2] >= 1:
            return True
    return False

def trueIsBabygin(cnts):
    tri = 0
    run = 0
    i = 0
    while i < 10:
        if cnts[i] >= 3:
            cnts[i] -= 3
            tri += 1
            continue
        if cnts[i] >= 1 and cnts[i+1] >= 1 and cnts[i+2] >= 1:
            cnts[i] -= 1
            cnts[i+1] -= 1
            cnts[i+2] -= 1
            run += 1
            continue
        i += 1
    if tri + run == 2:
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))

    p1_cnts = [0] * 12
    p2_cnts = [0] * 12
    winner = 0
    for i in range(0, 12, 2):
        n1 = lst[i]
        n2 = lst[i+1]
        p1_cnts[n1] += 1
        p2_cnts[n2] += 1

        if isBabygin(p1_cnts):
            winner = 1
            break

        if isBabygin(p2_cnts):
            winner = 2
            break
    
    print(f'#{tc} {winner}')