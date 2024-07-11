
#! CHECKING IF TWINKLE IS PRESENT IN THE FILE
# f = open("poem.txt")
# data = f.read()

# if ("twinkle" in data):
#     print("Yes")
# else:
#     print("No")

# f.close()



#! GENERATE SCORE AND UPDATE HIGHSCORE ACCORDINGLY
# import random
# def game():
#     score =  random.randint(0, 100)
#     print("You are playing the game")
#     print(f"Your score is {score}")
    
#     # Fetch high score
#     with open("highScore.txt") as f:
#         highScore = f.read()
#         if (highScore == ""):
#             highScore = 0
#         else:
#             highScore = int(highScore)
    
#     if (score > highScore or score == 0):
#         with open("highScore.txt", "w") as f:
#             f.write(str(score))

#     print("Game over")



# game()






#! GENERATE TABLES FROM 2 TO 20 INSIDE TEXT FILES 
# def generateTable(n):
#     table = " "
#     for i in range(1,11):
#         table += f"{n} x {i} = {n*i}\n" 
    
#     with open(f"Tables/table_{n}.txt", "w") as f:
#         f.write(table)

# for i in range(2,21):
#     generateTable(i)





#! FIND "DONKEY" WORD FROM A FILE AND UPDATE ALL "DONKEY" WITH "######"
# word = "Donkey"

# with open("Donkey.txt") as f:
#     data = f.read()

# data = data.replace(word, "######")

# with open("Donkey.txt", "w") as f:
#     f.write(data)


#! DO ABOVE PROGRAM FOR MULTIPLE WORDS 
# words = ["Donkey","is","kind"]

# with open("Donkey.txt") as f:
#     data = f.read()

# for word in words:
#     data = data.replace(word, "#"*len(word))

# with open("Donkey.txt", "w") as f:
#     f.write(data)



#! FIND PYHTON KEYWORD IS PRESENT IN LOG.HTML AND ALSO FIND ITS LINENO.

# with open("log.html") as f:
#     lines = f.readlines()
#     for line in lines :
#         if ("python" in line):
#             print(line)
#             print(lines.index(line)+1)
#             break
#     else:
#         print("Not found")




#! CREATE COPY OF LOG.HTML FILE
# with open("log.html") as f:
#     data = f.read()

# with open("log_copy.html", "w") as f:
#     f.write(data)




#! COMPARE LOG.HTML AND LOG_COPY.HTML
# with open("log.html") as f:
#     data = f.read()

# with open("log_copy.html") as f:
#     data_copy = f.read()

# if (data == data_copy):
#     print("Files are same")
# else:
#     print("Files are different")



#! Wipe out log_copy.html file
# with open("log_copy.html", "w") as f:
#     f.write("")


#! Rename Donkey.txt to donkey.txt
import os
os.rename("donkey.txt", "Donkey.txt")