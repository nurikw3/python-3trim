class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.__major = major

    def get_major(self):
        return self.__major

    def set_major(self, major):
        self.__major = major

    def display_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Major: {self.get_major()}")


s = Student("ALICE", 20, "Computer Science")
s.display_info()
