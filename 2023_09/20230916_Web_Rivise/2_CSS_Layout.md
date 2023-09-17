# CSS Layout

## CSS Box Model
모든 HTML 요소를 사각형 박스로 표현하는 개념

### 구성 요소

#### CSS Box Model
모든 HTML 요소를 사각형 박스로 표현하는 개념<br>
<span style="color:red">→ 내용(content), 안쪽 여백(padding)<br>
테두리(border), 외부 간격(margin)으로 구성되는 개념</span>

#### Box 구성 요소
Margin: 박스와 다른 요소 사이의 공백 가장 바깥쪽 영역<br>
Border: 콘텐츠와 패딩을 감싸는 테두리 영역<br>
Padding: 콘텐츠 주위에 위치하는 공백 영역<br>
Content: 콘텐츠가 표시되는 영역<br>

#### Box 구성 요소 예시
```html
<body>
  <div class="box1">box1</div>
  <div class="box2">box2</div>
</body>
```
```css
.box1 {
  width: 200px;
  padding-left: 25px;
  padding-bottom: 25px;
  margin-left: 25px;
  margin-top: 50px;
  border-width: 3px;
  border-style: solid;
  border-color: black;
}

.box2 {
  width: 200px;
  padding: 25px 50px;
  margin: 25px auto;
  border: 1px dashed black;
}
```

#### width & height 속성
요소의 너비와 높이를 지정<br>
이때 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함

#### CSS가 width 값을 계산하는 기준
CSS는 border가 아닌 content의 크기를 width 값으로 지정

#### box-sizing 속성
```css
* {
  box-sizing: content-box;
}
```
```css
* {
  box-sizing: border-box;
}
```

#### box-sizing 예시
```html
<body>
  <div class="box content-box">content-box</div>
  <div class="box border-box">border-box</div>
</body>
```
```css
.box {
  width: 100px;
  border: 2px solid black;
  padding: 10px;
  margin: 20px;
  background-color: lightgray;
}

.content-box {
  box-sizing: content-box;
}

.border-box {
  box-sizing: border-box;
}
```

### 박스 타입
Block & Inline
```css
.index {
  display: block;
}
```
```css
.index {
  display: inline;
}
```
#### Normal flow
CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향

#### 박스 타입 예시
```html
<h1>Normal flow</h1>
<p>Lorem, ipsum dolor sit amet consect explicabo</p>
<div>
  <p>block 요소는 기본적으로 부모 요소의 너비 100%를 차지하며, 자식 콘텐츠의 최대 높이를 취한다.</p>
  <p>block 요소의 총 너비와 총 높이는 content + padding + border width/height다.</p>
</div>
<p>block 요소는 서로 margins로 구분된다.</p>
<p>inline 요소는 <span>이 것처럼</span> 자체 콘텐츠의 너비와 높이만 차지한다.
  그리고 inline 요소는 <a href="#">width나 height 속성을 지정 할 수 없다.</a>
</p>
<p>
  물론 이미지도 <img src="#"> 인라인 요소다.
  단, 이미지는 다른 inline 요소와 달리 width나 height로 크기를 조정할 수 있다.
</p>
<p>
  만약 inline 요소의 크기를 제어하려면 block 요소로 변경하거나 inline-block 요소로 설정해주어야 한다.
</p>
```
```css
a,
span,
img {
  border: 3px solid red;
}

h1,
p,
div {
  border: 1px solid blue;
}
```

#### block 타입 특징
- 항상 새로운 행으로 나뉨
- width와 height 속성을 사용하여 너비와 높이를 지정할 수 있음
- 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로<br>
사용 가능한 공간을 모두 차지함<br>
(너비를 사용가능한 공간의 100%로 채우는 것)
- 대표적인 block 타입 태그
  - h1~6, p, div

#### inline 타입 특징
- 새로운 행으로 나뉘지 않음
- width와 height 속성을 사용할 수 없음
- 수직 방향
  - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음
- 수평 방향
  - padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그
  - a, img, span

#### 속성에 따른 수평 정렬
```
좌로 정렬
margin-right: auto;
text-align: left;

우로 정렬
margin-left: auto;
text-align: right;

가운데 정렬
margin-right: auto;
margin-left: auto;
text-align: center;
```

### 기타 display 속성
1. inline-block
2. none

#### 'inline-block'
- inline과 block 요소 사이의 중간 지점을 제공하는 display 값
- block 요소의 특징을 가짐
  - width 및 height 속성 사용 가능
  - padding, margin 및 border 로 인해 다른 요소가 밀려남

#### 'inline-block' 예시
```html
<!-- 1. 이제 다른 요소를 밀어낼 수 있는 span -->
<p>Lorem ipsum dolor sit amet <span>consectetur</span> adipisicing elit. Animi iusto enim officia exercitationem
  dolorque, quasi velit, dolores, tempora illum odio necessitatibus. Fugit,
  cumque eligendi!</p>

<!-- 2. 리스트 요소를 가로로 정렬 -->
<ul>
  <li><a href="#">link</a></li>
  <li><a href="#">link</a></li>
  <li><a href="#">link</a></li>
</ul>

<!-- 3. div 요소를 가로로 정렬 -->
<div class="container">
  <div class="box"></div>
  <div class="box"></div>
  <div class="box"></div>
</div>
```
```css
span {
  margin: 20px;
  padding: 20px;
  width: 80px;
  height: 50px;
  background-color: lightblue;
  border: 2px solid blue;
  display: inline-block;
}

ul>li {
  background-color: crimson;
  padding: 10px 20px;
  display: inline-block;
}

.container {
  text-align: center;
}

.box {
  display: inline-block;
  width: 100px;
  height: 100px;
  background-color: #4CAF50;
  margin: 10px;
}
```

#### 'none'
- 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

#### 'none' 예시
```html
<div class="box">1</div>
<div class="box none">2</div>
<div class="box">3</div>
```
```css
.box {
  width: 100px;
  height: 100px;
  background-color: red;
  border: 2px solid black;
}

.none {
  display: none;
}
```

## CSS Layout Position
CSS Layout<br>
각 요소의 <span style="color:red">위치</span>와 <span style="color:red">크기를 조정</span>하여 웹 페이지의 디자인을 결정하는 것<br>
Display, Position, Float, Flexbox 등

### CSS Position
CSS Position<br>
요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것<br>
다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등

#### Position 이동 방향
- top
- left
- right
- bottom
- Z Axis

#### Position 유형
1. static
2. relative
3. absolute
4. fixed
5. sticky

#### Position 예시
```html
<div class="container">
  <div class="box static">Static</div>
  <div class="box absolute">Absolute</div>
  <div class="box relative">Relative</div>
  <div class="box fixed">Fixed</div>
</div>
```
```css
* {
  box-sizing: border-box;
}

body {
  height: 1500px;
}

.container {
  /* position: relative;는 absolute 블럭의 기준점을 만들어 주기 위함 */
  position: relative;
  height: 300px;
  width: 300px;
  border: 1px solid black;
}

.box {
  height: 100px;
  width: 100px;
  border: 1px solid black;
}

.static {
  /* static은 기본값입니다 */
  position: static;
  background-color: lightcoral;
}

.absolute {
  /* 절대적 위치 (기존의 자신이 사용한 영역을 버리게 된다) */
  /* 기준점을 static이 아닌 부모를 찾아 올라간다 */
  position: absolute;
  background-color: lightgreen;
  top: 100px;
  left: 100px;
}

.relative {
  /* 상대위치, 기준점=(본인의 static 시점의 위치) */
  position: relative;
  background-color: lightblue;
  top: 100px;
  left: 100px;
}

.fixed {
  /* 집나간 친구.. */
  position: fixed;
  background-color: gray;
  top: 0;
  right: 0;
}
```

#### Position 예시 - sticky
```html
<h1>Sticky positioning</h1>
<div>
  <div class="sticky">첫 번째 Sticky</div>
  <div>
    <p>내용1</p>
    <p>내용2</p>
    <p>내용3</p>
  </div>
  <div class="sticky">두 번째 Sticky</div>
  <div>
    <p>내용4</p>
    <p>내용5</p>
    <p>내용6</p>
  </div>
  <div class="sticky">세 번째 Sticky</div>
  <div>
    <p>내용7</p>
    <p>내용8</p>
    <p>내용9</p>
  </div>
</div>
```
```css
body {
  height: 1500px;
}

.sticky {
  position: sticky;
  /* top: 0 라는 임계점에 도달하면 fixed 수행 */
  top: 0;
  background-color: lightblue;
  padding: 20px;
  border: 2px solid black;
}
```

#### Position 유형별 특징
- static
  - 기본값
  - 요소를 Normal Flow에 따라 배치
- relative
  - 요소를 Normal Flow에 따라 배치
  - 자기 자신을 기준으로 이동
  - 요소가 차지하는 공간은 static일 때와 같음
- absolute
  - 요소를 Normal Flow에서 제거
  - 가장 가까운 relative 부모 요소를 기준으로 이동
  - 문서에서 요소가 차지하는 공간이 없어짐
- fixed
  - 요소를 Normal Flow에서 제거
  - 현재 화면영역(viewport)을 기준으로 이동
  - 문서에서 요소가 차지하는 공간이 없어짐
- sticky
  - 요소를 Normal Flow에 따라 배치
  - 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면 그 위치에서 고정됨(fixed)
  - 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체
    - 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문

# absolute 예시
```html
<div class="card">
  <div class="card-content">
    <h3>Card Title</h3>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <span class="badge">New</span>
  </div>
</div>
```
```css
.card {
  width: 300px;
  height: 200px;
  border: 1px solid black;
  position: relative;
}

.card-content {
  padding: 10px;
}

.badge {
  background-color: red;
  color: white;
  padding: 5px 10px;
  position: absolute;
  top: 0;
  right: 0;
}
```
#### z-index
요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정

#### z-index 특징
- 정수 값을 사용해 Z축 순서를 지정
- 더 큰 값을 가진 요소가 작은 값의 요소를 덮음

#### z-index 예시
```html
<div class="container">
  <div class="box red"></div>
  <div class="box green"></div>
  <div class="box blue"></div>
</div>
```
```css
.container {
  position: relative;
}

.box {
  position: absolute;
  width: 100px;
  height: 100px;
}

.red {
  background-color: red;
  top: 50px;
  left: 50px;
  z-index: 3;
}

.green {
  background-color: green;
  top: 100px;
  left: 100px;
  z-index: 2;
}

.blue {
  background-color: blue;
  top: 150px;
  left: 150px;
  z-index: 1;
}
```

## CSS Layout Flexbox

### 구성 요소

### 레이아웃 구성