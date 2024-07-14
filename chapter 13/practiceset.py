# name = input("Enter your name: ")
# marks = int(input("Enter your marks: "))
# PhoneNo = int(input("Enter your phone number: "))

# print("Your name is {} and your marks is {} and your phone number is {}".format(name, marks, PhoneNo))





# table = [str(7*i) for i in range(1,11)]
# s = "\n".join(table)
# print(s)




# def divisible5(n):
#     if(n%5 == 0):
#         return True
#     else:
#         return False

# a = [1,2,3,4,5,6,7,8,9,10]
# b = list(filter(divisible5,a))
# print(b)





# from functools import reduce
# def MaxNo(a,b):
#     if(a>b):
#         return a
#     else:
#         return b

# list = [34,23,12,56,78,90]

# print(reduce(MaxNo,list))






from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run()