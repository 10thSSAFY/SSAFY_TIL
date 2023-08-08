for _ in range(10):
    T = int(input())
    word = input()
    data = input()
    ans = 0
    for i in range(len(data) - len(word)):
        if data[i:i+len(word)] == word:
            ans += 1

    print(f'#{T} {ans}')

'''
1
ab
abcdab
'''