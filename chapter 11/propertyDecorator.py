class Employee:
    a = 4
    
    @classmethod
    def show(cls):
        print(cls.a)  
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, name):
        self.fname = name.split()[0]
        self.lname = name.split()[1]


e = Employee()
e.a = 5
e.show() 

e.name = "Alex kumar"
print(e.name)