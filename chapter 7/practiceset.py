# n = int(input("Enter a number: "))
# for i in range(11):
#     print(f"{n} x {i} = {n*i}")


# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l :
#     if(name.startswith("S")):
#         print(f"Hello {name}")
        


#! print star pattern
'''
    *
   ***
  *****
 *******
'''
# n = 3
# for i in range(n):
#     print(" "*(n-i-1) + "*"*(2*i+1))


# for i in range(n):
#     print("*"*(i+1))


# for i in range(n):
#     if(i==0 or i==n-1):
#         print("*"*n)
#     else:
#         print("*" + " "*(n-2) + "*")



#! print same pattern using ''''end=""'''' keyword

n = 5

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()


for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()


for i in range(n):
    if(i==0 or i==n-1):
        for j in range(n):
            print("*", end="")
    else :
        print("*", end="")
        for j in range(n-2):
            print(" ", end="")
        print("*", end="")
    print()