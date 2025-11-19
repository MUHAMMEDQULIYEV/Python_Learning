"""
in that file i want to learn property method

"""


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deletion of fullname")
        self.first = None
        self.last = None


emp1 = Employee("Mahammad", "Quliyev")
emp1.fullname = "Corey Shaffer"
print(emp1.first)
print(emp1.last)
print(emp1.email)
