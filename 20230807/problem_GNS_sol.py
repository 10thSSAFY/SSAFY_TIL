# GNS
import sys
sys.stdin = open('res/input_GNS.txt', 'r')

pattern = ['zro', 'one']
original = list('zro zro'.split())

result = []
for n in original:
    for i in range(3):
        if pattern[i] == n:
            result.append(i)
            break

patten = {'ZRO':0, 'ONE':1}
for n in original:
    result.append(pattern[i])