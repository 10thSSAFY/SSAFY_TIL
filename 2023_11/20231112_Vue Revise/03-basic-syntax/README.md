# Computed Properties

## Computed
- `computed()`
    - 계산된 속성을 정의하는 함수
    - 미리 계산된 속성을 사용하여 템플릿에서<br>
    표현식을 단순하게 하고 불필요한 반복 연산을 줄임

## computed 기본 예시
- 할 일이 남았는지 여부에 따라 다른 메시지를 출력하기
```js
const todos = ref([
  { text: 'Vue 실습' },
  { text: '자격증 공부' },
  { text: 'TIL 작성' }
])
```
```html
<h2>남은 할 일<h2>
<p>{{ todos.length > 0 ? '아직 남았다' : '퇴근' }}</p>
```
- 템플릿이 복잡해지며 todos에 따라 계산을 수행하게 됨
- 만약 이 계산을 템플릿에 여러 번 사용하는 경우에는 반복이 발생
- computed 적용
- 반응성 데이터를 포함하는 복잡한 로직의 경우 computed를 활용하여 미리 값을 계산

## computed 특징
- 반환되는 값은 computed ref이며 일반 refs와 유사하게 계산된 결과를<br>
`.value`로 참조 할 수 있음 (템플릿에서는 .value 생략 가능)
- computed 속성은 의존된 반응형 데이터를 <span style="color: crimson">자동으로 추적</span>
- 의존하는 데이터가 변경될 때만 재평가
    - restOfTodos의 계산은 todos에 의존하고 있음
    - 따라서 <span style="color: crimson">todos가 변경될 때만 restOfTodos가 업데이트 됨</span>
    ```js
    const restOfTodos = computed(() => {
      return todos.value.length > 0 ? '아직 남았다' : '퇴근'
    })
    ```
    