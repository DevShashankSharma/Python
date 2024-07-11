'''
1 for snake
-1 for water
0 for gun
'''

import random

computerChoice = random.randint(-1, 1)
revDict = {1: "s", -1: "w", 0: "g"}

yourStr = input("Enter your choice: ")
yourDict = {"s": 1, "w": -1, "g": 0}
yourChoice = yourDict.get(yourStr)

print(f"Computer choice is {revDict[computerChoice]} and your choice is {yourStr}")

# if (computerChoice == yourChoice):
#     print("Tie")
# elif (computerChoice == 1 and yourChoice == -1):
#     print("Computer win")
# elif (computerChoice == 1 and yourChoice == 0):
#     print("Your win")
# elif (computerChoice == -1 and yourChoice == 1):
#     print("Your win")
# elif (computerChoice == -1 and yourChoice == 0):
#     print("Computer win")
# elif (computerChoice == 0 and yourChoice == 1):
#     print("Computer win")
# elif (computerChoice == 0 and yourChoice == -1):
#     print("Your win")
# else:
#     print("Invalid input")




#! Another way
if(computerChoice-yourChoice == 1 or computerChoice-yourChoice == -2):
    print("Computer win")
elif(yourChoice-computerChoice == 1 or yourChoice-computerChoice == -2):
    print("Your win")
else:
    print("Tie")