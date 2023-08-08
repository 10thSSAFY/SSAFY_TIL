# 회문 2
import sys
sys.stdin = open('res/input_1216.txt', 'r')

def is_palindrome(line):
    return line == line[::-1]

def max_pdr(arr, d):
    for line in arr:
        for i in range(101 - d):
            if is_palindrome(line[i:i+d]):
                return d
    return 1

def find_max_pdr(arr):
    max_pdr_length = 1
    for i in range(2, 101):
        if i > max_pdr_length + 2:
            break
        if max_pdr_length < max_pdr(arr, i):
            max_pdr_length = i
    return max_pdr_length

for tc in range(1, 11):
    N = int(input())
    rows = [input().strip() for _ in range(100)]
    columns = [''.join(x) for x in zip(*rows)]
 
    result = max(find_max_pdr(rows), find_max_pdr(columns))
 
    print(f'#{tc} {result}')
