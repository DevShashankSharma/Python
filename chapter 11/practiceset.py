# class TwoDvector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(self.x, self.y)


# class ThreeDvector(TwoDvector):
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z

#     def show(self):
#         print(self.x, self.y, self.z)


# v = ThreeDvector(1, 2, 3)
# v.show()
# s = TwoDvector(4, 5)
# s.show()





# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(self.name)

# class Pet(Animal):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def show(self):
#         print(self.name)

# class Dog(Pet):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def show(self):
#         print(self.name)
    
#     @staticmethod
#     def bark():
#         print("barking")


# d = Dog("Alex")
# d.bark()





# class Employee:
#     salary = 10000
#     increment = 20
    
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary + self.salary * (self.increment/100)

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, value):
#         self.increment = (value/self.salary - 1)*100 

# e = Employee()
# print(e.salaryAfterIncrement)

# e.salaryAfterIncrement = 20000
# print(e.increment)






# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def __add__(self, obj):
#         return Complex(self.real + obj.real, self.img + obj.img)
    
#     def __mul__(self, obj):
#         return Complex(self.real * obj.real - self.img * obj.img, self.real * obj.img + self.img * obj.real)
#     def __str__(self):
#         return f"{self.real} + {self.img}j"



# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# c3 = c1 + c2
# print(c3)

# c4 = c1 * c2
# print(c4)







class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, obj):
        return vector(self.x + obj.x, self.y + obj.y, self.z + obj.z)

    def __mul__(self, obj):
        return self.x * obj.x + self.y * obj.y + self.z * obj.z
    
    def __len__(self):
        l = [self.x, self.y, self.z]
        return len(l)

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)

v3 = v1 + v2
print(v3)

print(v1 * v2)
print(len(v1))