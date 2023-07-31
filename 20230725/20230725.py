# .discard()
my_set = {1, 2, 3}
my_set.discard(2)

print(my_set)  # {1, 3}

# my_set.remove(10)  # KeyError: 10
print(my_set.discard(10))  # None

#-----------------------------------#

# .pop()
my_set = {1, 2, 3}
element = my_set.pop()

print(element)  # 1
print(my_set)  # {2, 3}

#---------리스트, 딕셔너리---------#

# 리스트 -> 선형탐색
b = {
    '삼계탕': 20000,
    '육전': 15000
}
# 세트요소 & 딕셔너리 키 -> 해시함수 -> 해시 테이블
# 문자는 완전 랜덤 -> 숫자는 어느 정도 순서를 갖춤
# By "arbitrary" the docs don't not mean "random"
print(hash(1))
print(hash(1))
print(hash('a'))
print(hash('a'))
# 해시 가능성(hasha)은 객체를 "딕셔너리의 키"나 "세트의 요소"로 사용할 수 있게 하는데,
# 이 자료 구조들이 내부적으로 해시 값을 사용하기 때문

# 해시 충돌

my_set = {1, 2, 3}
my_set.update([4, 5, 1])
print(my_set)  # {1, 2, 3, 4, 5}


set1 = {0, 1, 2, 3, 100}
set2 = {0, 2, 3, 4, 99, 200}

print(set1.union(set2))  # {0, 1, 2, 3, 100, 99, 4, 200}

#-------------------------------------------#

# D.get(k)
my_dict = {'name': 'Alice'}

print(my_dict['name'])  # Alice
print(my_dict.get('name'))  # Alice

# 찾고자 하는 키가 없을 때
# print(my_dict['age'])  # KeyError
print(my_dict.get('age'))  # Unknown
print(my_dict.get('age', 'Unknown'))  # Unknown

#--------------------------------------#

# D.keys()
person = {'name': 'Alice', 'age': 25}

print(person.keys())  # dict_keys(['name', 'age'])
for key in person.keys():
    print(key)
"""
name
age
"""
print(person.values())  # dict_values(['Alice', 25])
for value in person.values():
    print(value)
"""
Alice
25
"""
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

#-----------------------------#

# D.pop()
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person.pop('country', 'country 키는 없어요'))  # country 키는 없어요

#---------------------------#

# [], .get(), .setdefault() practice
# 혈액형 인원 수 세기
# 결과 = {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# []
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    # 기존에 키가 이미 존재한다면,
    if blood_type in new_dict:
        # 기존에 키의 값을 +1 증가
        new_dict[blood_type] += 1
    # 키가 존재하지 않는다면 (처음 설정되는 키)
    else:
        new_dict[blood_type] = 1
print(new_dict)  # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}

# .get()
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
print(new_dict)  # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}

# .setdefault()
new_dict = {}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
print(new_dict)  # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}

#-----------------------------------#

# 슬라이싱 copy
a = [1, 2, 3]
b = a[:]
b[0] = 100

c = a.copy()
c[0] = 100
print(a, b, c)  # [1, 2, 3] [100, 2, 3] [100, 2, 3]


# 얕은 복사의 한계
a = [1, 2, [1, 2]]

b = a[:]
b[2][0] = 999
print(a, b)  # [1, 2, [999, 2]] [1, 2, [999, 2]]

# copy
a = [1, 2, [1, 2]]
c = a.copy()
c[2][0] = 999
print(a, c) # [1, 2, [999, 2]] [1, 2, [999, 2]]


# 깊은 복사
import copy

original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[2][0] = 999
print(original_list, deep_copied_list)  # [1, 2, [1, 2]] [1, 2, [999, 2]]

