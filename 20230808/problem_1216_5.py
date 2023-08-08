# 회문 2
import sys
sys.stdin = open('res/input_1216.txt', 'r')

for _ in range(10):
    tc = input()
    words = [input().strip() for _ in range(100)]

    result = 0

    for word in words:
        for i in range(100):
            for j in range(100-i):
                new_word = word[j:j+i+1]
                if new_word == new_word[::-1] and result < i+1:
                    result = i+1
                    break
    
    for n in range(100):
        new_str = ''
        for word in words:
            new_str += word[n]
        for i in range(100):
            for j in range(100-i):
                new_word = new_str[j:j+i+1]
                if new_word == new_word[::-1] and result < i+1:
                    result = i+1
                    break

    print(f'#{tc} {result}')
