
#! lamda function
# def square(x):
#     return x*x

# square = lambda x: x*x

# print(square(5))




#! join method
# a = ["hello", "how", "are", "you"]

# final = " ".join(a)
# print(final)



#! format method
# a = "{} is a {} language".format("Python", "high level")
# b = "{1} is a {0} language".format("Python", "high level")
# c = "{name} is a {language} language".format(name = "Python", language = "high level")

# print(a)
# print(b)
# print(c)



#! map filter reduce
from functools import reduce


l = [1,2,3,4,5,6,7,8,9,10]
square = lambda x: x*x

sqList = list(map(square, l))
print(sqList)



def isEven(x):
    return x%2 == 0

evenList = list(filter(isEven, l))
print(evenList)



def sum(x, y):
    return x+y

sumList = reduce(sum, l)
print(sumList)