class Person:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        raise NotImplementedError


class Teacher(Person):
    def get_role(self):
        return f"{self.name} is a Teacher"


class Student(Person):
    def get_role(self):
        return f"{self.name} is a Student"


class School:
    def __init__(self):
        self.members = []

    def add(self, person):
        self.members.append(person)

    def show(self):
        for m in self.members:
            print(m.get_role())


s = School()
s.add(Teacher("Alice"))
s.add(Student("Bob"))
s.show()
