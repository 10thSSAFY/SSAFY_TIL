# Classes [Home](./..)

## 객체지향 프로그래밍

### 개요
#### 절차 지향 프로그래밍 `Procedural Programming`
프로그램을 ‘데이터’와 ‘절차’로 구성하는 방식의 프로그래밍 패러다임

#### 절차 지향 프로그래밍 특징
- "데이터"와 해당 데이터를 처리하는 "함수(절차)"가 분리되어 있으며, <br>함수 호출의 흐름이 중요
- 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행
- 실제로 실행되는 내용이 무엇이 무엇인가가 중요
- 데이터를 다시 재사용하거나 하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식

![image](https://github.com/ragu6963/TIL/assets/32388270/cc0db5a1-8200-409b-8b90-c42ea7823c71)

#### 소프트웨어 위기(Software Crisis)
- 하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 <br>증가함에 따라 소프트웨어에 발생한 충격
![image](https://github.com/ragu6963/TIL/assets/32388270/e251d24f-781d-46ca-b6dd-56f1c2c8e9d1)

#### 객체 지향 프로그래밍 `Object Oriented Programming`
데이터와 해당 데이터를 조작하는 메서드를 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임

#### 절차 지향 vs 객체 지향
- 절차 지향
    - 데이터와 해당 데이터를 처리하는 <br>함수(절차)가 분리
    - 함수 호출의 흐름이 중요
    ![image](https://github.com/ragu6963/TIL/assets/32388270/f84ff2d6-f73e-4105-9528-ad17a7e7174d)
    
- 객체 지향
    - 데이터와 해당 데이터를 처리하는 <br>메서드(메시지)를 하나의 객체(클래스)로 묶음
    - 객체 간 상호작용과 메시지 전달이 중요
    ![image](https://github.com/ragu6963/TIL/assets/32388270/7430654c-d52d-4cf8-9ae4-af83f38369b8)

## 객체
### 개요
#### 클래스 `Class`
- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공
    ![image](https://github.com/ragu6963/TIL/assets/32388270/2f87ae3c-ce62-4a81-983e-06073f5f9745)

#### 객체 `Object`
클래스에서 정의한 것을 토대로 메모리에 할당된 것
<span style='color:red;'>‘속성’</span>과 <span style='color:red;'>‘행동’</span>으로 구성된 모든 것

#### 객체 예시
![image](https://github.com/ragu6963/TIL/assets/32388270/1e728c44-90e5-4acc-99bb-a4ab1998c3b9)

#### 클래스와 객체
- 클래스로 만든 객체를 <span style='color:red;'>인스턴스</span> 라고도 함
    ![image](https://github.com/ragu6963/TIL/assets/32388270/f3447cce-fcab-4f66-81da-3047c77df12b)


- 변수 name의 타입은 str 클래스다.
- 변수 name은 <span style='color:red;'>str 클래스의 인스턴스</span>이다.
- 우리가 사용해왔던 <span style='color:red;'>데이터 타입은 사실 모두 클래스</span>였다.
    ```py
    name = 'Alice'

    print(type(name))  # <class 'str'>
    ```
- 결국 문자열 타입의 변수는 str 클래스로 만든 인스턴스다.
    ```py
    print(help(str))

    """
    class str(object)
     |  str(object='') -> str
     |  str(bytes_or_buffer[, encoding[, errors]]) -> str
     |
     |  Create a new string object from the given object. If encoding or
     |  errors is specified, then the object must expose a data buffer
     |  that will be decoded using the given encoding and error handler.
     |  Otherwise, …
    """
    ```

```py
'' 
'hello' 
'파이썬'
# 문자열 타입(클래스)의 객체(인스턴스)
```

```py
[1, 2, 3] 
[1]
[]
['hi']

# 리스트 타입(클래스)의 객체(인스턴스)
```

#### 인스턴스와 메서드
 
```py
“hello”.upper()

"""
문자열.대문자로()

객체.행동()

인스턴스.메서드()
"""
```

```py
[1, 2, 3].sort()

"""
리스트.정렬해()

객체.행동()

인스턴스.메서드()
"""
```

> 하나의 객체(object)는 특정 타입의 인스턴스(instance)이다. 
- 123, 900, 5는 모두 `int`의 인스턴스
- 'hello', 'bye'는 모두 `string`의 인스턴스
- [232, 89, 1], []은 모두 `list`의 인스턴스

#### 객체(object)의 특징
- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

    ![image](https://github.com/ragu6963/TIL/assets/32388270/dfed70e3-bc37-45ef-988a-b6becc4806b8)

## 클래스
### 개요
#### 클래스 `Class`
- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공

#### 클래스 구조
```py
# 클래스 정의
class Person:
    pass

# 인스턴스 생성
iu = Person()

# 메서드 호출
iu.메서드()

# 속성(변수) 접근
iu.attribute
```

#### 클래스 기본 활용
```py
# 클래스 정의
class Person:
    blood_color = 'red'

    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다.'


# 인스턴스 생성
singer1 = Person('iu')

# 메서드 호출
print(singer1.singing())  # iu가 노래합니다.

# 속성(변수) 접근
print(singer1.blood_color)  # red
```

#### 클래스 기본 활용 1
- 생성자 함수
    - 객체를 생성할 때 자동으로 호출되는 <br>특별한 메서드
    - __init__이라는 이름의 메서드로 <br>정의되며, 객체의 초기화를 담당
    - 생성자 함수를 통해 인스턴스를 <br>생성하고 필요한 초기값을 설정

    ```py
    class Person:
    """
    생성자 함수
    """
    def __init__(self, name):
        self.name = name


    # 인스턴스 생성
    singer1 = Person('iu')
    ```

#### 클래스 기본 활용 2
- 인스턴스 변수
    - 인스턴스(객체)마다 별도로 <br>유지되는 변수
    - 인스턴스마다 독립적인 값을 가지며, <br>인스턴스가 생성될 때마다 초기화됨

    ```py
    class Person:
    def __init__(self, name):
        self.name = name  # 인스턴스 변수 name


    singer1 = Person('iu')
    
    # 인스턴스 변수
    print(singer1.name)
    ```

#### 클래스 기본 활용 3

- 클래스 변수
    - 클래스 내부에 선언된 변수
    - 클래스로 생성된 모든 인스턴스들이<br>공유하는 변수

    ```py
    class Person:
    blood_color = 'red'  # 클래스 변수 blood_color

    def __init__(self, name):
        self.name = name


    singer1 = Person('iu')
    print(singer1.name)

    # 클래스 속성(변수) 접근
    print(singer1.blood_color)

    ```

#### 클래스 기본 활용 4

- 인스턴스 메서드
    - 각각의 인스턴스에서 <br>호출할 수 있는 메서드
    - 인스턴스 변수에 접근하고 <br>수정하는 등의 작업을 수행

    ```py
    class Person:
        blood_color = 'red'

        def __init__(self, name):
            self.name = name

        """
        인스턴스 메서드
        """
        def singing(self):
            return f'{self.name}가 노래합니다.'


    singer1 = Person('iu')

    # 인스턴스 메서드 호출
    print(singer1.singing())

    print(singer1.blood_color)

    ```

#### 인스턴스와 클래스 간의 이름 공간(namespace)
- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 <span style='color:red;'>독립적인</span> 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색
    ![image](https://github.com/ragu6963/TIL/assets/32388270/f1476ead-aff8-47ac-9118-b1e8095751e0)

```py
# Person 정의
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)


p1 = Person()
p1.talk()  # unknown
"""
p1은 인스턴스 변수가 정의되어 있지 않아
클래스 변수(unknown)가 출력됨
"""

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown
p2.name = 'Kim'
p2.talk()  # Kim
"""
p2는 인스턴스 변수가 정의되어
인스턴스 변수(Kim)가 출력됨
"""

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim
"""
Person 클래스의 값이 Kim으로 변경된 것이 아닌
p2 인스턴스의 이름 공간에 name이 Kim으로 저장됨
"""
```

![image](https://github.com/ragu6963/TIL/assets/32388270/70a65cb1-e567-4792-8b1d-ddebeb618958)

#### 독립적인 이름공간을 가지는 이점
- 각 인스턴스는 독립적인 메모리 공간을 가지며, <br>클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능
- 객체 지향 프로그래밍의 중요한 특성 중 하나로, <br>클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장
- 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 <br>서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음
> 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌

### 인스턴스 변수와 클래스 변수
#### 클래스 변수 활용
- 가수가 몇 명인지 확인하고 싶다면?
    - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정할 수 있음
    ```py
    class Person:
        count = 0
        
        def __init__(self, name):
            self.name = name
            Person.count += 1
        
        
    person1 = Person('iu')
    person2 = Person('BTS')
        
    print(Person.count)  # 2
    ```

#### 클래스 변수와 인스턴스 변수
- 클래스 변수를 변경할 때는 항상 <span style='color:red;'>클래스.클래스변수</span> 형식으로 변경
- 예시 1

    ```py
    class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r


    c1 = Circle(5)
    c2 = Circle(10)
    print(Circle.pi)  # 3.14
    print(c1.pi)  # 3.14
    print(c2.pi)  # 3.14 
    ```
- 예시 2

    ```py
    class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r 


    c1 = Circle(5)
    c2 = Circle(10)
    Circle.pi = 5  # 클래스 변수 변경
    print(Circle.pi)  # 5
    print(c1.pi)  # 5
    print(c2.pi)  # 5 
    ```
- 예시 3 

    ```py
    
    class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r 


    c1 = Circle(5)
    c2 = Circle(10)
    c2.pi = 5  # 인스턴스 변수 변경
    print(Circle.pi)  # 3.14 (클래스 변수)
    print(c1.pi)  # 3.14 (클래스 변수)
    print(c2.pi)  # 5 (새로운 인스턴스 변수가 생성됨)
    ```

### 실행 해보기
```python
# 실행 해보기 1
class Person:
    blood_color = 'red'

    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다.'


singer1 = Person('iu')

print(singer1.singing())

print(singer1.blood_color)
```

```python
# 실행 해보기 2
# Person 정의
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)


p1 = Person()
p1.talk()  

p2 = Person()
p2.talk() 
p2.name = 'Kim'
p2.talk() 

print(Person.name) 
print(p1.name)
print(p2.name)
```

```python
# 실행 해보기 3
class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    
person1 = Person('iu')
person2 = Person('BTS')
    
print(Person.count) 
```

```python
# 실행 해보기 4
class Circle:
  pi = 3.14

  def __init__(self, r):
    self.r = r


c1 = Circle(5)
c2 = Circle(10)
print(Circle.pi)
print(c1.pi)  
print(c2.pi)  
```

```python
# 실행 해보기 5
class Circle:
  pi = 3.14

  def __init__(self, r):
    self.r = r

c1 = Circle(5)
c2 = Circle(10)
Circle.pi = 5  
print(Circle.pi) 
print(c1.pi)   
print(c2.pi)   
```

```python
# 실행 해보기 6
class Circle:
  pi = 3.14

  def __init__(self, r):
    self.r = r

c1 = Circle(5)
c2 = Circle(10)
c2.pi = 5   
print(Circle.pi)  
print(c1.pi)  
print(c2.pi)  
```

## 메서드
### 개요
#### 메서드 종류
- 인스턴스 메서드
- 클래스 메서드
- 정적 메서드

    ![image](https://github.com/ragu6963/TIL/assets/32388270/c1c62879-9386-4b84-a4ab-d6d41aa56ad8)

### 인스턴스 메서드
#### 인스턴스 메서드 `instance method`
- 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
> 인스턴스의 상태를 조작하거나 동작을 수행

#### 인스턴스 메서드 구조
- 클래스 내부에 정의되는 메서드의 기본
- 반드시 첫 번째 매개변수로 <span style='color:red;'>인스턴스 자신(self)</span>을 전달받음

    ```py
    class MyClass:

        def instance_method(self, arg1, ...):
            pass
    ```

#### self 동작 원리
- upper 메서드를 사용해 문자열 ‘hello’를 대문자로 변경하기
    ```py
    'hello'.upper()
    ```

- 하지만 실제 파이썬 내부 동작은 다음과 같이 이루어진다.
    ```py
    str.upper('hello')
    ```

- str 클래스가 upper 메서드를 호출했고, <br>그 첫번째 인자로 문자열 인스턴스가 들어간 것이다.

> <span style='color:red;'>인스턴스 메서드의 첫번째 매개변수가 반드시 인스턴스 자기 자신인 이유</span>

- `'hello'.upper()` 은 `str.upper('hello')`를 <br>객체 지향 방식의 메서드로 호출하는 표현이다. (단축형 호출)

- ‘hello’라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자가 아닌<br>객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적 표현이다.

#### 생성자 메서드 `constructor method`
인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
> 인스턴스 변수들의 초기값을 설정

#### 생성자 메서드 구조
```py
class Person:
    def __init__(self):
        print('인스턴스가 생성되었습니다.')


person1 = Person()  # 인스턴스가 생성되었습니다.

class Person:
    def __init__(self, name):
        print(f'인스턴스가 생성되었습니다. {name}')


person1 = Person('지민')  # 인스턴스가 생성되었습니다. 지민
```

### 클래스 메서드
#### 클래스 메서드 `class method`
클래스가 호출하는 메서드
> 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

#### 클래스 메서드 구조
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 호출하는 클래스(cls)가 전달됨

    ```py
    class MyClass:
        
        @classmethod  # @ <- 데코레이터
        def class_method(cls, arg1, ...):  # cls -> MyClass
            pass

    ```

#### 클래스 메서드 예시
```py
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')  # Person.count를 쓸 수도 있지만 상속때문에 필요할 수 있음.


person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population() # 인구수는 2입니다.
```

### 스태틱 메서드
#### 스태틱(정적) 메서드 `static method`
클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드

> 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 <br>필요하지 않은 경우에 사용

#### 스태틱 메서드 구조
- @staticmethod 데코레이터를 사용하여 정의
- 호출 시 필수적으로 작성해야 할 매개변수가 없음
- 즉, 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을<br>위한 메서드로 사용
    ```py
    class MyClass:
        
        @staticmethod
        def static_method(arg1, ...):
            pass
    ```

#### 스태틱 메서드 예시

```py
class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        return string.capitalize()


text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text) # dlrow ,olleh

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text) # Hello, world

```

### 메서드 정리
#### 메서드 정리
- 인스턴스 메서드
    - 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행

- 클래스 메서드
    - 인스턴스의 상태에 의존하지 않는 기능을 정의
    - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

- 스태틱 메서드
    - 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

#### 각자의 역할
- 클래스가 사용해야 할 것
    - 클래스 메서드
    - 스태틱 메서드

- 인스턴스가 사용해야 할 것
    - 인스턴스 메서드

#### 메서드 정리 예시
```py
class MyClass:

    def instance_method(self):
        return 'instance method', self
        
    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'
```

#### 클래스가 할 수 있는 것
- 클래스는 모든 메서드를 호출 할 수 있음
- <span style='color:red;'>하지만 클래스는 클래스 메서드와 스태틱 메서드만 사용하도록 한다</span>

    ```py
    instance = MyClass()

    print(MyClass.instance_method(instance))  # ('instance method', <__main__.MyClass object at0x…028F10>)
    print(MyClass.class_method())  # ('class method', <class '__main__.MyClass'>)
    print(MyClass.static_method())  # static method
    ```

#### 인스턴스가 할 수 있는 것
- 인스턴스는 모든 메서드를 호출 할 수 있음
- <span style='color:red;'>하지만 인스턴스는 인스턴스 메서드만 사용하도록 한다</span>

    ```py
    instance = MyClass()

    print(instance.instance_method())  # ('instance method', <__main__.MyClass object at 0x0000…84EAF10>)
    print(instance.class_method())  # ('class method', <class '__main__.MyClass'>)
    print(instance.static_method())  # static method
    ```

#### 할 수 있다 != 써도 된다
각자의 메서드는 OOP 패러다임에 따라 <br>명확한 목적에 따라 설계된 것이기 때문에 <br>클래스와 인스턴스 각각 올바른 메서드만 사용하도록 해야 한다.

### 실행 해보기
```python
# 실행 해보기 1
class Person:
    def __init__(self):
        print('인스턴스가 생성되었습니다.')


person1 = Person()

class Person:
    def __init__(self, name):
        print(f'인스턴스가 생성되었습니다. {name}')


person1 = Person('지민')
```

```python
# 실행 해보기 2
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')


person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population()
```

```python
# 실행 해보기 3
class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        return string.capitalize()


text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text) 

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text) 
```

## 상속
### 개요
#### 상속 `Inheritance`
기존 클래스의 속성과 메서드를 물려받아 <br>
새로운 하위 클래스를 생성하는 것

#### 상속이 필요한 이유
1. 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
    - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, <br>중복된 코드를 줄일 수 있음
2. 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고, <br>더 구체적인 클래스를 만들 수 있음
3. 유지 보수의 용이성
    - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 <br>되므로 유지 보수가 용이해짐 
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

![image](https://github.com/ragu6963/TIL/assets/32388270/f259eed5-c629-4a42-b0cc-4896162169c8)

### 클래스 상속

#### 상속 없이 구현 하는 경우 (1/2)
- 학생/교수 정보를 나타내기 어려움

    ```py
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')


    s1 = Person('김학생', 23)
    s1.talk() # 반갑습니다. 김학생입니다.

    p1 = Person('박교수', 59)
    p1.talk() # 반갑습니다. 박교수입니다.
    ```

#### 상속 없이 구현 하는 경우 (2/2)
- 메서드 중복 정의
    ```py
    class Professor:
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department

        def talk(self): # 중복
            print(f'반갑습니다. {self.name}입니다.')

    class Student:
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa

        def talk(self): # 중복
            print(f'반갑습니다. {self.name}입니다.')
    ```

#### 상속을 사용한 계층구조 변경
![image](https://github.com/ragu6963/TIL/assets/32388270/ecdca0f0-47ce-4afc-853d-fa0d4575b458)
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self): # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.
```

#### super()
부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수

#### super() 사용 예시
- 사용 전

    ```py
    class Person:
        def __init__(self, name, age, number, email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email


    class Student(Person):
        def __init__(self, name, age, number, email, student_id):
            self.name = name
            self.age = age
            self.number = number
            self.email = email
            self.student_id = student_id
    ```

- 사용 후

    ```py
    class Person:
        def __init__(self, name, age, number, email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email


    class Student(Person):
        def __init__(self, name, age, number, email, student_id):
            # 부모클래스의 init 메서드 호출
            super().__init__(name, age, number, email)
            self.student_id = student_id
    ```

### 다중 상속
#### 다중 상속
- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 <span style='color:red;'>상속 순서에 의해 결정</span>됨

#### 다중 상속 예시
```py
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # XY
```

#### 상속 관련 함수와 메서드
- mro() 
    - Method Resolution Order
    - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 <br>상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

    ```py
    print(FirstChild.mro())

    # [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]
    ```

### 실행 해보기
```python
# 실행 해보기 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

p1.talk()
s1.talk()
```

```python
# 실행 해보기 2
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry()) 
print(baby1.swim()) 
print(baby1.walk()) 
print(baby1.gene) 
```

## 참고
#### 매직 메서드
- 특별한 인스턴스 메서드
- <span style='color:red;'>특정 상황에 자동으로 호출되는 메서드</span>
- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
    - 스페셜 메서드 혹은 매직 메서드라고 불림
- 예시
    ```py 
    __str__(self)
    __len__(self)__
    __lt__(self, other)
    __le__(self, other)
    __eq__(self, other)
    __gt__(self, other)
    __ge__(self, other)
    __ne__(self, other)
    ```

#### 매직 메서드 예시
```py
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def __str__(self):
        return f'[원] radius: {self.r}'

c1 = Circle(10)
c2 = Circle(1)

print(c1) # [원] radius: 10
print(c2) # [원] radius: 1
```

#### 데코레이터 (Decorator)
- 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

    ```py
    """
    데코레이터 정의
    """
    def my_decorator(func):
        def wrapper():
            # 함수 실행 전에 수행할 작업
            print('함수 실행 전')
            # 원본 함수 호출
            result = func()
            # 함수 실행 후에 수행할 작업
            print('함수 실행 후')
            return result
        return wrapper

    """
    데코레이터 정의
    """
    @my_decorator
    def my_function():
        print('원본 함수 실행')

    my_function()

    """
    함수 실행 전
    원본 함수 실행
    함수 실행 후
    """
    ```

#### 절차 지향과 객체 지향은 대조되는 개념이 아니다
객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해<br>
객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임 

#### 실행 해보기
```python
# 실행 해보기 1
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def __str__(self):
        return f'[원] radius: {self.r}'

c1 = Circle(10)
c2 = Circle(1)

print(c1) 
print(c2) 
```

```python
# 실행 해보기 2
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')

        # 원본 함수 호출
        result = func()
        
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result
    return wrapper

@my_decorator
def my_function():
    print('원본 함수 실행')

my_function()

"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""
```