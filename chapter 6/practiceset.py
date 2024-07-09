
#! WAP to find largest number from 4 numbers
a1 = int(input("Enter first no : "))
a2 = int(input("Enter second no : "))
a3 = int(input("Enter third no : "))
a4 = int(input("Enter fourth no : "))

if(a1>a2 and a1>a3 and a1>a4):
    print(a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print(a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print(a3)
else:
    print(a4)
    
    
#! WAP to check if percentage is greater than 40 and each mark is greater than 30
mark1 = int(input("Enter first mark : "))
mark2 = int(input("Enter second mark : "))
mark3 = int(input("Enter third mark : "))

# total percentage
total = mark1 + mark2 + mark3
# percentage
percentage = (total / 300) * 100

# mark1 percentage
per1 = (mark1 / 100) * 100
# mark2 percentage
per2 = (mark2 / 100) * 100
# mark3 percentage
per3 = (mark3 / 100) * 100

# if percentage is greater than 40 and each per is greater than 30
if(percentage > 40 and per1 > 30 and per2 > 30 and per3 > 30):
    print("Pass")
else:
    print("Fail")



#! . A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
comment = input("Enter a comment: ")


if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("This is a spam comment")
else:
    print("This is not a spam comment")
    

#! Write a program to find whether a given username contains less than 10 characters or not.
userName = input("Enter your name: ")

if(len(userName) < 10):
    print("Your name is less than 10 characters")
else:
    print("Your name is greater than 10 characters")
    


#! Write a program which finds out whether a given name is present in a list or not.
name = input("Enter your name: ")
names = ["Alex", "Bob", "Cathy", "David"]
if(name in names):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")



#! Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter your post: ")
if("harry" in post.lower()):
    print("Your post is talking about Harry")
else:
    print("Your post is not talking about Harry")