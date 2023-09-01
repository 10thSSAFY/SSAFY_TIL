# k번째로 작은 원소를 찾는 알고리즘
def select(arr, k):
    for i in range(0, k):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr[k-1]


lst = [11, 22, 10, 64, 25]
result = select(lst, 3)
print(lst)  # [10, 11, 22, 64, 25]  # 3번째 까지 정렬된 결과
print(result)  # 22  # 3번째로 작은 수