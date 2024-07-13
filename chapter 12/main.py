
# #! Walrus operator
# if (n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")
# # Output: List is too long (5 elements, expected <= 3) 



# #! Type defination

# a: int = 10
# b: str = "10"
# c: float = 10.0
# d: bool = True

# def sum(a: int, b: int) -> int:
#     return a + b


# sum(10, 20)



# from typing import List, Tuple, Dict, Union
# # List of integers
# numbers: List[int] = [1, 2, 3, 4, 5]
# # Tuple of a string and an integer
# person: Tuple[str, int] = ("Alice", 30)
# # Dictionary with string keys and integer values
# scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# # Union type for variables that can hold multiple types
# identifier: Union[int, str] = "ID12"





#! Match case

# a = 10
# match a:
#     case 10:
#         print("10")
#     case 20:
#         print("20")
#     case _:
#         print("Not 10 or 20")



#! Exception handling
# try:
#     a = int(input("Enter a number: "))
#     print(a)
# except ValueError as v:
#     print(v)
# except Exception as e:
#     print(e)




#! Raise exception
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if(b == 0):
#     raise ZeroDivisionError("Cannot divide by zero")
# else:
#     print(f"The division of {a} and {b} is {a/b}")




#! try-except-else
# try:
#     a = int(input("Enter a number: "))
#     print(a) 
# except Exception as e:
#     print(e)
# else:
#     print("No exception") # run if else execute successfully


#! finally
# try:
#     a = int(input("Enter a number: "))
#     print(a) 
# except Exception as e:
#     print(e)
# else:
#     print("No exception") # run if else execute successfully
# finally:
#     print("Always execute")  # always execute


# def main():
#     try:
#         a = int(input("Enter a number: "))
#         print(a) 
#         return
#     except Exception as e:
#         print(e)
#         return 
#     finally:
#         print("Always execute")  # always execute even you return from try block or except block 

# main()





#! IF __NAME__== ‘__MAIN__’ IN PYTHON
# from module import myFunc




#! Global variable 
# a = 10
# def myFunc():
#     # global a
#     a = 20
#     print(a)
# myFunc() 
# print(a)




#! Enumerate
list = ["apple", "banana", "cherry"]

# index = 0
# for item in list:
#     print(f"The item at index {index} is {item}")
#     index += 1

#? This can be simplified using enumerate function

for index, item in enumerate(list):
    print(f"The item at index {index} is {item}")





#! List comprehension
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Squaredlist = []
# for item in mylist:
#     Squaredlist.append(item**2)
# print(Squaredlist)

# Squaredlist = [item**2 for item in mylist]
# print(Squaredlist)

list = [item**2 for item in mylist if item % 2 == 0]
print(list)