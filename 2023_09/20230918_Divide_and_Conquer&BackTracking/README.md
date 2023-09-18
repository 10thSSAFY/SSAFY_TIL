# 알고리즘 기법의 종류

1. 전체를 다 보자(Brute Force - 완전 탐색)
  - 배열: 반복문 다 돌리기
  - 그래프: DFS, BFS
2. 상황마다 좋은 걸 고르기
  - 규칙을 찾는 것
  - 주의사항: 항상 좋은 것을 뽑아도, 최종 결과가 제일 좋다. = 보장 되지 않는다.
3. 하나의 큰 문제를 작은 문제로 나누어 부분적으로 해결하자 (Dynamic Programming)
  - Memoization 기법을 활용
  - 점화식(bottom-up), 재귀(top-down)
4. 큰 문제를 작은 문제로 쪼개서 해결하자
  - (Devide and Conquer - 분할 정복)
5. 전체 중, 가능성 없는 것을 빼고 보자
  - (Backtracking - 백트래킹)
  - 가지치기

# 분할 정복 기법
## 설계 전략
- 분할(Divide): 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복(Conquer): 나눈 작은 문제를 각각 해결한다.
- 통합(Combine): (필요하다면) 해결된 해답을 모은다.

## 분할 정복 기반의 알고리즘
C^8 = C * C * C * C * C * C * C * C
C^8 = C^4 * C^4 = (C^4)^2 = (((C^2)^2)^2)
C^n = C^(((n-1)/2)*2)*C
```
def Recursive_Power(x, n):
  if n == 1:
    return x
  if n is even:
    y <- Recursive_Power*(x, n/2)
    return y * y
  else:
    y <- Recursive_Power(x, (n-1)/2)
    reutrn y * y * x
```

# 병합 정렬
- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄.
  - top-down 방식
- 시간 복잡도
  - O(n log n)

## 알고리즘: 분할 과정
```
merge_sort(LIST m)
  IF length(m) == 1 : RETURN m

  LIST left, right
  middle <- length(m) / 2
  FOR x in m befor middle
    add x to right
  
  left <- merge_sort(left)
  right <- merge_sort(right)

  RETURN merge(left, right)
```

```
merge(LIST left, LIST right)
  LIST result

  WHILE length(left) > 0 OR length(right) > 0
    IF length(left) > 0 AND length(right) > 0
      IF first(left) <= first(right)
        append popfirst(left) to result
      else:
        append popfirst(right) to reuslt
    ELIF length(left) > 0
      append popfirst(left) to result
    ELIF length(right) > 0
      append popfirst(right) to result
  RETURN result
```

# 퀵 정렬
- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
  - 병합 정렬과 동일?
- 다른 점1: 병합 정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.
- 다른 점2: 각 부분 정렬이 끝난 후, 병합정렬은 "병합"이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다.

# 분할 정복의 활용
- 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘이다. 또한, 멀티코어(Multi-Core) CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용된다.
- 퀵 정렬은 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘이다.


### 퀵 정렬
- 직접 구현할 일은 적다
  - 평균적으로 굉장히 좋음 O(NlogN)
  - 특히, 큰 데이터를 다룰 때 좋다.
  - 단점: 역순 정렬 등 최악의 경우 O(N^2)
- 과거에 면접 단골 질문 + 분할 정복 학습에 좋다.
  - 코드를 보기 전에 반드시 손으로 직접 해보기

### 이진검색
- 코딩 테스트의 메인 알고리즘 중 하나
- 목적: "원하는 값을 빨리 찾는 것"
- 시간: O(logN)
- Parametric Search
  - lower bound
  - upper bound
    - 여러 개의 데이터 중 2가 처음 나온 시점
    - 2~9 사이의 데이터는 몇 개인가?