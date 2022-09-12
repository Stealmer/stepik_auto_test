class Person:
 
    def __init__(self, name):
        self.name = name   # имя человека
 
 
    def display_info(self):
        print(f"Name: {self.name} ")
 
 
class Employee():
 
    def work(self):
        print(f"{self.name} works")

class Student(Person, Employee):
 
    def study(self):
        print(f"{self.name} study") 
 
tom = Employee("Tom")
print(tom.name)     # Tom
tom.display_info()  # Name: Tom 
tom.work()          # Tom works
tom.study()