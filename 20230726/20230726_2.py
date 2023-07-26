# Person 정의
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)


p1 = Person()
p1.talk()  # unknown <- 클래스 변수, 본인의 인스턴스가 없으면 일단 클래스 변수로 찾아 나간다.

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown

p2.name = 'Kim'  # <- 본인의 인스턴스 변수가 있기 때문에 클래스 변수를 찾아가지 않는다.
p2.talk()  # Kim

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim

p1.address = 'Korea'  # p1에 address 변수가 생긴다.
print(p1.address)  # Korea