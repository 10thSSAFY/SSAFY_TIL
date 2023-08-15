# 토너먼트 카드게임
import sys
sys.stdin = open('res/input_4880.txt', 'r')

def winner(lst):
    if len(lst) == 1:
        return lst.pop()
    if len(lst) == 2:
        if [lst[0][0], lst[1][0]] == [1, 1]:
            return lst[0]
        elif [lst[0][0], lst[1][0]] == [1, 2]:
            return lst[1]
        elif [lst[0][0], lst[1][0]] == [1, 3]:
            return lst[0]
        elif [lst[0][0], lst[1][0]] == [2, 1]:
            return lst[0]
        elif [lst[0][0], lst[1][0]] == [2, 2]:
            return lst[0]
        elif [lst[0][0], lst[1][0]] == [2, 3]:
            return lst[1]
        elif [lst[0][0], lst[1][0]] == [3, 1]:
            return lst[1]
        elif [lst[0][0], lst[1][0]] == [3, 2]:
            return lst[0]
        elif [lst[0][0], lst[1][0]] == [3, 3]:
            return lst[0]
    else:
        if len(lst) % 2 == 0:
            lst1 = lst[:len(lst)//2]
            lst2 = lst[len(lst)//2:]
        else:
            lst1 = lst[:len(lst)//2+1]
            lst2 = lst[len(lst)//2+1:]
        return winner([winner(lst1), winner(lst2)])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    new_lst = []
    idx = 0
    for l in lst:
        new_lst.append([l, idx])
        idx += 1
    result = winner(new_lst)
    print(f'#{tc} {result[1]+1}')
