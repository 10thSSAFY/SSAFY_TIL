# 베이비진 게임 (야매풀이)
import sys
sys.stdin = open('res/input_5203.txt', 'r')

T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    lst_a = [0]*10
    lst_b = [0]*10
    A = B = 0
    cnt_a = cnt_b = 0
    for i in range(0, 12, 2):
        if A > 0 or B > 0:
            break
        lst_a[lst[i]] += 1
        lst_b[lst[i+1]] += 1

        for j in range(len(lst_a)):
            if lst_a[j] == 3:
                A += 1
                break
            if lst_b[j] == 3:
                B += 1
                break

        if A > 0 or B > 0:
            break

        for j in range(len(lst_a)):
            if lst_a[j] != 0:
                cnt_a += 1
                if cnt_a == 3:
                    A += 1
                    break
            else:
                cnt_a = 0

            if lst_b[j] != 0:
                cnt_b += 1
                if cnt_b == 3:
                    B += 1
                    break
            else:
                cnt_b = 0

        if A > 0 or B > 0:
            break
        
    if A > B:
        print(f'#{t} 1')
    elif A == B:
        print(f'#{t} 0')
    else:
        print(f'#{t} 2')