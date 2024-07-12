# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

# p = Programmer("Alex", 120000, 1234)
# print(p.name, p.salary, p.pin)






# class Calculator:
#     def __init__(self, num):
#         self.num = num

#     def square(self):
#         return self.num ** 2

#     def cube(self):
#         return self.num ** 3

#     def squareroot(self):
#         return self.num ** 0.5
    
#     @staticmethod
#     def greet():
#         print("Good Morning")

# a = Calculator(9)
# print(a.square())
# print(a.cube())
# print(a.squareroot())




#! Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

# class demo:
#     a = 4

# o = demo()
# o.a = 0
# print(o.a) # print the instance attribute because instance attribute is present
# print(demo.a) # print the class attribute

#! No, it doesn't change the class attribute but it set the object attribute






# from random import randint
# class Train:
#     def __init__(self, trainNo):
#         self.trainNo = trainNo
#     def booking(self, fro , to):
#         print(f"Booking is confirmed for train number {self.trainNo} from {fro} to {to}")

#     def getStatus(self):
#         print(f"Train number {self.trainNo} is running on time")

#     def getFare(self, fro , to):
#         print(f"Rs. {randint(1000,5000)} will be charged for train number {self.trainNo} from {fro} to {to}")


# t1 = Train(1234)
# t1.booking("Delhi" , "Mumbai")
# t1.getStatus()
# t1.getFare("Delhi" , "Mumbai")





from random import randint
class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    def booking(Alex, fro , to):
        print(f"Booking is confirmed for train number {Alex.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train number {self.trainNo} is running on time")

    def getFare(self, fro , to):
        print(f"Rs. {randint(1000,5000)} will be charged for train number {self.trainNo} from {fro} to {to}")


t = Train(1234)
t.booking("Delhi" , "Mumbai")
t.getStatus()
t.getFare("Delhi" , "Mumbai")