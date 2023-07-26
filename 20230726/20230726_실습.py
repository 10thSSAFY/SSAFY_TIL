class Student:
    sheet = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def attendant(self, date):
        print(f'{self.name} {date}에 출석')
        Student.sheet.append((self.name, date))

    def __str__(self):
        return f'{self.name} {self.age}'

    def __lt__(self, other):
        return self.age < other.age

    def __len__(self):
        return self.age

    @classmethod
    def getSheet(cls):
        return cls.sheet


s1 = Student('김씨', 20)
s2 = Student('박씨', 22)
print(s1.name, s2.name)
s1.attendant("2023-07-26")
s2.attendant("2023-07-26")
print(Student.getSheet())

print(s1)

print(s1<s2)

print(len(s1))