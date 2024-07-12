class Employee:
    company = "ITC"
    name = "Alex"
    def show(self):
        print(f"The name of employee is {self.name} and salary is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"The programmer is good in {self.language}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name of employee is {self.name} and salary is {self.salary}")
    
#     def showLanguage(self):
#         print(f"The name of employee is {self.name} and is good in {self.languages}")

class Programmer(Employee, Coder):
    # name = "Bob"
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name of employee is {self.name} and is good in {self.language}")


p1 = Programmer()
print(p1.company)
p1.show()
p1.showLanguage()
p1.printLanguage()