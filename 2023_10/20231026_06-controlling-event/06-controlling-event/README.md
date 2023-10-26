# 이벤트
## event
- 무언가 일어났다는 신호, 사건
  - 모든 DOM 요소는 이러한 event를 만들어 냄

- 이벤트 종류
  - mouse, input, keyboard, touch ...
  - https://developer.mozilla.org/en-US/docs/Web/API/Event

```
DOM 요소는 eneve를 받고 받은 event를 '처리' 할 수 있음
(event handler: 이벤트 처리기)
```

## event handler
- 이벤트가 발생했을 때 실행되는 함수
  - 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것

## .addEventListener()
- 대표적인 이벤트 핸들러 중 하나
  - 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것

### EvenvTarget.addEventListener(type, handler)
- EventTarget: DOM 요소
- type: 수신할 이벤트
- handler: 콜백 함수
```
대상에 특정 Event가 발생하면, 지정한 이벤트를 받아 할 일을 등록한다.
```

## .addEventListener(type, handler)
- type
  - 수신할 이벤트 이름
  - 문자열로 작성(ex. 'click')
- handler
  - 발생한 이벤트 객체를 수신하는 콜백 함수
  - 콜백 함수는 발생한 Event object를 유일한 매개변수로 받음

## addEventListener 활용
- "버튼을 클릯하면 버튼 요소 출력하기"
  - 버튼에 이벤트 처리기를 부착하여 클릭 이벤트가 발생하면 이벤트가 발생한 버튼정보를 출력
- 요소에 addEventListener를 부착하게 되면 내부의 this 값은 대상 요소를 가리키게 됨 (event 객체의 currentTarget  속성 값과 동일)

## 버블링
- 핸들러는 form 요소에 할당되어 있지만 div나 p 요소 같은 중첩된 요소를 클릭해도 동작함
  - 왜 div나 p를 클릭했는데 form에 할당된 핸들러가 동작할까?


## 'target' & 'currentTarget' 속성
- 'target' 속성
  - 이벤트가 발생한 가장 안쪽의 요소(target)를 참조하는 속성
  - 실제 이벤트가 시작된 target 요소
  - 버블링이 진행 되어도 변하지 않음

- 'currentTarget' 속성
  - '현재'요소
  - 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
  - 'this'와 같음

- 'target'
  - 실제 이벤트가 발생하는 요소를 가리킴

- 'currentTarget'
  - 핸들러가 연결된 outerouter 요소만을 가리킴

- 핸들러는 outerouter에 하나 밖에 없지만 이 핸들러에서 outerouter의 내부 모든 하위 요소에서 발생하는 클릭 이벤트를 잡아내고 있음

- 클릭 이벤트가 어디서 발생했든 상관없이 outerouter까지 이벤트가 버블링 되어 핸들러를 실행시키기 때문

# event handler 활용
