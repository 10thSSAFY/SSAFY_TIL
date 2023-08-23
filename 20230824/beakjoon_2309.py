import sys
sys.stdin = open('res/input_beakjoon_2309.txt', 'r')

def result(lst):
    for h1 in range(8):
        for h2 in range(h1+1, 9):
            if S - lst[h1] - lst[h2] == 100:
                lst.remove(lst[h2])
                lst.remove(lst[h1])
                return

lst = []
for _ in range(9):
    lst.append(int(input()))

S = sum(lst)
lst.sort()
result(lst)

for _ in range(7):
    print(lst.pop(0))
