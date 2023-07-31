# List Comprehension 구조
#   0 ~ 9 요소를 가지는 리스트 만들기
#       1. 일반적인 방법
new_list = []
for i in range(10):
    new_list.append(i)

print(new_list)

#       2. list comprehension
new_list_2 = [i for i in range(10)]
print(new_list_2)

#   0 ~ 9 요소중 홀수만 가지는 리스트 만들기
#       1. 일반적인 방법
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i)

print(new_list)

#       2. list comprehension
new_list_2 = [i for i in range(10) if i % 2 == 1]
print(new_list_2)

#       가독성 이슈
new_list_3 = []
for i in range(10):
    if i % 2 == 1:
        new_list_3.append(i)
    else:
        new_list_3.append(str(i))

print(new_list_3)

new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
print(new_list_3)

# 리스트를 생성하는 3가지 방법 비교
# 정수 1, 2, 3을 가지는 새로운 리스트 만들기
# 어떤게 제일 빨라요?
numbers = ['1', '2', '3']

# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# 2. map
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2)

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers ]
print(new_numbers_3)

# enumerate 예시
fruits = ['apple', 'banana', 'cherry']
print(enumerate(fruits))  # <enumerate object at 0x0000023c86ff4580>
print(list(enumerate(fruits)))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]  // 튜플

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')
