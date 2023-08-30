# 베이비진 게임
import sys
sys.stdin = open('res/input_5203.txt', 'r')

def game(r_lst):
    s_lst = sorted(r_lst)
    for i in range(len(r_lst)-2):
        if s_lst[i] == s_lst[i+1] and s_lst[i+1] == s_lst[i+2]:
            return True
    s_lst = sorted(list(set(r_lst)))
    if len(s_lst) >= 3:
        for i in range(len(s_lst)-2):
            if s_lst[i+2] - s_lst[i+1] == 1 and s_lst[i+1] - s_lst[i] == 1:
                return True
    return False
 
 
T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    p1 = lst[0:3:2]
    p2 = lst[1:4:2]
    result = 0
    for i in range(4):
        p1.append(lst[i*2 + 4])
        if game(p1):
            result = 1
            break
        p2.append(lst[i*2 + 5])
        if game(p2):
            result = 2
            break
    print(f'#{tc} {result}')