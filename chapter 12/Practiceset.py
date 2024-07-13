try :
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try :
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try :
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thanks")








l = [1,2,3,4,5,6,7,8,9,10]

for i,item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)






n = 5
table = [n*i for i in range(1,11)]
# print(table)
with open("chapter 12/tables.txt","a") as f:
    f.write(str(table) + "\n")




try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")