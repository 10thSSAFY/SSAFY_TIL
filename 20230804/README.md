# 복습
## 버블정렬
```python
lst = [55, 7, 78, 12, 42]

def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

print(lst)
BubbleSort(lst, 5)
print(lst)
'''
[55, 7, 78, 12, 42]
[7, 12, 42, 55, 78]
'''
```

```
BubbleSort([55, 7, 78, 12, 42], 5)
        for 4 in range(4, 0, -1):
                for 0 in range(0, 4):
                        if 55 > 7:
                                55, 7 = 7, 55
                                [7, 55, 78, 12, 42]
                for 1 in range(0, 4):
                        if 55 > 78:
                for 2 in range(0, 4):
                        if 78 > 12:
                                78, 12 = 12, 78
                                [7, 55, 12, 78, 42]
                for 3 in range(0, 4):
                        if 78 > 42:
                                78, 42 = 42, 78
                                [7, 55, 12, 42, 78]
        for 3 in range(4, 0, -1):
                for 0 in range(0, 3):
                        if 7 > 55:
                for 1 in range(0, 3):
                        if 55 > 12:
                                55, 12 = 12, 55
                                [7, 12, 55, 42, 78]
                for 2 in range(0, 3):
                        if 55 > 42:
                                55, 42 = 42, 55
                                [7, 12, 42, 55, 78]
        for 2 in range(4, 0, -1):
                for 0 in range(0, 2):
                        if 7 > 12:
                for 1 in range(0, 2):
                        if 12 > 42:
        for 1 in range(4, 0, -1):
                for 0 in range(0, 1):
                        if 7 > 12:
```
## 배열 선언
```
3
1 2 3
4 5 6
7 8 9
```
```python
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
```
```
3
123
456
789
```
```python
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
```

## 배열 순회
- n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법
### 행 우선 순회
```python
# i 행의 좌표
# j 열의 좌표

for i in range(n):
    for j in range(m):
        print(Array[i][j])  # 필요한 연산 수행
```
### 열 우선 순회
```python
# i 행의 좌표
# j 열의 좌표

for j in range(m):
    for i in range(n):
        print(Array[i][j])  # 필요한 연산 수행
```
### 지그재그 순회
```python
# i 행의 좌표
# j 열의 좌표

for i in range(n):
    for j in range(m):
        print(Array[i][j + (m-1-2*j) * (i%2)])
        # 필요한 연산 수행
```
### 델타를 이용한 2차 배열 탐색
- 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
```
arr[0 ... N-1][0 ... N-1]  # NxN 배열
di[] <- [0, 1, 0, -1]
dj[] <- [1, 0, -1, 0]
for i : 0 -> N-1 :
    for j : 0 -> N-1:
        for k in range(4):
            ni <- i + di[k]
            nj <- j + dj[k]
            if 0<=ni<N and 0<=nj<N  # 유효한 인덱스면
                print(arr[ni][nj])
```
### 전치행렬
```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]]  # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```
```
1 2 3       1 4 7
4 5 6  ->   2 5 8
7 8 9       3 6 9
```
## 비트 연산자
### 부분집합 생성 방법
```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)  # n: 원소의 개수

for i in range(1<<n):  # 1<<n : 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1<<j):  # i의 j번 비트가 1인 경우
            print(arr[j], end=", ")  # j번 원소 출력
    print()
print()
```
## 정렬되어 있지 않은 경우, 순차탐색
```
def sequentialSearch(a, n, key)
    i <- 0
    while i<n and a[i] != key :
        i <- i+1
    if i<n :
        return i
    else:
        return -1
```
## 정렬되어 있는 경우, 순차탐색
```
def sequentialSearch2(a, n, key)
    i <- 0
    while i<n and a[i]<key :
        i <- i+1
    if i<n and a[i] == key :
        return i
    else :
        return -1
```
## 이진 검색 알고리즘
```python
def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:  # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False  # 검색 실패
```
## 선택 정렬
```python
lst = [55, 7, 78, 12, 42]

def SelectionSort(arr, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(lst)
SelectionSort(lst, 5)
print(lst)
```
```
SelectionSort([55, 7, 78, 12, 42], 5):
        for 0 in range(4)
                minIdx = 0
                for 1 in range(1, 5)
                        if 55 > 7
                                minIdx = 1
                for 2 in range(1, 5)
                        if 7 > 78
                for 3 in range(1, 5)
                        if 7 > 12
                for 4 in range(1, 5)
                        if 7 > 42
                55, 7 = 7, 55
                [7, 55, 78, 12, 42]
        for 1 in range(4)
                minIdx = 1
                for 2 in range(2, 5)
                        if 55 > 78
                for 3 in range(2, 5)
                        if 55 > 12
                                minIdx = 3
                for 4 in range(2, 5)
                        if 12 > 42
                55, 12 = 12, 55
                [7, 12, 78, 55, 42]
        for 2 in range(4)
                minIdx = 2
                for 3 in range(3, 5)
                        if 78 > 55
                                minIdx = 3
                for 4 in range(3, 5)
                        if 55 > 42
                                minIdx = 4
                78, 42 = 42, 78
                [7, 12, 42, 55, 78]
        for 3 in range(4)
                minIdx = 3
                for 4 in range(4, 5)
                        if 55 > 78
                55, 55 = 55, 55
                [7, 12, 42, 55, 78]
                
[7, 12, 42, 55, 78]
```