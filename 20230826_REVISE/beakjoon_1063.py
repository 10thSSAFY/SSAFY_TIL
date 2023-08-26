# 킹
import sys
sys.stdin = open('res/input_beakjoon_1063.txt', 'r')
input = sys.stdin.readline

def itoa(num):
    return chr(ord('A')-1+num)

def atoi(alphabet):
    return ord(alphabet) - ord('A') + 1

pos = {'R':[0, 1], 'L':[0, -1], 'B':[-1, 0], 'T':[1, 0],
       'RT':[1,1], 'LT':[1,-1], 'RB':[-1,1], 'LB':[-1,-1]}


king, stone, N = input().split()
kingR, kingC = [int(king[1]), atoi(king[0])]
stoneR, stoneC = [int(stone[1]), atoi(stone[0])]
# print(kingR, kingC)
# print(stoneR, stoneC)

for _ in range(int(N)):
    r, c = pos[input().strip()]
    new_kingR, new_kingC = kingR+r, kingC+c
    if 1 <= new_kingR < 9 and 1 <= new_kingC < 9:
        if (new_kingR, new_kingC) == (stoneR, stoneC):
            new_stoneR, new_stoneC = stoneR+r, stoneC+c
            if 1 <= new_stoneR < 9 and 1 <= new_stoneC < 9:
                kingR, kingC, stoneR, stoneC = new_kingR, new_kingC, new_stoneR, new_stoneC
        else:
            kingR, kingC = new_kingR, new_kingC

print(itoa(kingC)+str(kingR))
print(itoa(stoneC)+str(stoneR))
