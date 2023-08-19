# 버블 정렬 알고리즘
def BubbleSort(a, N):  # 정렬할 List, N 원소 수  # 정렬할 배열과 배열의 크기
    for i in range(N-1, 0, -1):  # 범위의 끝 위치  # 정렬될 구간의 끝
        for j in range(0, i):  # 비교할 원소 중 왼쪽 원소의 인덱스
            if a[j] > a[j+1]:  # 왼쪽 원소가 더 크면
                a[j], a[j+1] = a[j+1], a[j]


lst = [55, 7, 78, 12, 42]
N = len(lst)
BubbleSort(lst, N)

print(lst)  # [7, 12, 42, 55, 78]
