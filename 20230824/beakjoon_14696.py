import sys
sys.stdin = open('res/input_beakjoon_14696.txt', 'r')
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    A, *A_lst = input().split()
    B, *B_lst = input().split()
    if A_lst.count('4') != B_lst.count('4'):
        if A_lst.count('4') > B_lst.count('4'):
            print('A')
        else:
            print('B')
    elif A_lst.count('3') != B_lst.count('3'):
        if A_lst.count('3') > B_lst.count('3'):
            print('A')
        else:
            print('B')
    elif A_lst.count('2') != B_lst.count('2'):
        if A_lst.count('2') > B_lst.count('2'):
            print('A')
        else:
            print('B')
    elif A_lst.count('1') != B_lst.count('1'):
        if A_lst.count('1') > B_lst.count('1'):
            print('A')
        else:
            print('B')
    else:
        print('D')
