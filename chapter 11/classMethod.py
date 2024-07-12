class Employee:
    a = 4
    
    @classmethod
    def show(cls):
        print(cls.a)
    
    def show2(self):
        print(self.a)


e = Employee()
e.a = 5
e.show()
e.show2()