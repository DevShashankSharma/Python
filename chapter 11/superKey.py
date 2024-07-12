
#! example of super keyword
class Employee:
    company = "ITC"
    name = "Alex"
    def __init__(self) :
        print("I am init method")
    def show(self):
        print(f"The name of employee is {self.name} and salary is {self.company}")

class Coder(Employee):
    language = "Python"
    def __init__(self):
        super().__init__()
        print("I am init method of Coder")
    def printLanguage(self):
        print(f"The programmer is good in {self.language}")


p1 = Coder()