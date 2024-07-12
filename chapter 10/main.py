class Employee: 
    languages = ["Python", "Java", "C++"]
    salary = 1000
    
    def __init__(self, name, salary, languages):  #! constructor or dunder method which is call automatically
        self.name = name
        self.salary = salary
        self.languages = languages
    
    def getInfo(self): 
        print(f"The name of employee is {self.name} and languages known are {self.languages} and salary is {self.salary}")
    
    def greet(self):
        print(f"Good Morning {self.name}")
    
    @staticmethod
    def sayHello():
        print("Hello")


# e1 = Employee() 
# e1.name = "Alex"
# print(e1.name, e1.languages, e1.salary) 
# e1.getInfo()  #! it can be written as e1.getInfo(e1)
# e1.greet()
# e1.sayHello()

# e2 = Employee() 
# e2.name = "Bob"
# e2.languages = "JavaScript"
# print(e2.name, e2.languages, e2.salary)
#! Here "name" is "instance attribute" and "salary" and "languages" is "class attribute"
#! Instance attribute > class attribute


alex = Employee("Alex", 120000, "Python")
alex.getInfo()