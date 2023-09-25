# 서로 다른 N개의 원소 중 M개를 순서 없이 골라낸 것: 조합(Combination)
def Comb(k, s):
    if k == M:
        print(result)
        return
    for i in range(s, N-M+1+k):
        result[k] = lst[i]
        Comb(k + 1, i + 1)


N = 5
M = 3
lst = [1, 2, 3, 4, 5]
result = [0] * M

Comb(0, 0)

'''
[1, 2, 3]
[1, 2, 4]
[1, 2, 5]
[1, 3, 4]
[1, 3, 5]
[1, 4, 5]
[2, 3, 4]
[2, 3, 5]
[2, 4, 5]
[3, 4, 5]
'''
