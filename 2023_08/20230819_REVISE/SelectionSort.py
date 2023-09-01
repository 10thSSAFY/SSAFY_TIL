# 선택 정렬 알고리즘
def SelectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]

lst = [64, 25, 10, 22, 11]
N = len(lst)
SelectionSort(lst, N)

print(lst)  # [10, 11, 22, 25, 64]
