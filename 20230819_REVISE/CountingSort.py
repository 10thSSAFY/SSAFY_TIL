# 카운팅 정렬 알고리즘
def CountingSort(A, B, k):
    # A [] = 입력 배열(0 to k)
    # B [] = 정렬된 배열.
    # C [] = 카운트 배열.
    C = [0] * (k+1)

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]


lst = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(lst)
sorted_lst = [0] * N
CountingSort(lst, sorted_lst, N)

print(sorted_lst)  # [0, 1, 1, 1, 2, 3, 4, 4]
