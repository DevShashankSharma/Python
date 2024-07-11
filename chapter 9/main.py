# f = open("file.txt")
# data = f.read()
# print(data)
# f.close() 

# st = "Hey how are you"
# f = open("file.txt", "w")
# f.write(st)
# f.close()

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close() 




#! using readlines function
# f = open("file.txt")
# # lines = f.readlines()
# # print(lines,type(lines))


#! using readline function
# line1 = f.readline()
# print(line1,type(line1))
# line2 = f.readline()
# print(line2)
# f.close()


#! using loop
# f = open("file.txt")
# line = f.readline()
# while line != "":
#     print(line)
#     line = f.readline()
# f.close()


#! Append mode
# f = open("file.txt", "a")
# f.write("\nI am fine")
# f.close()


#! with statement  --> automatically closes the file and do same thing
with open("file.txt") as f:
    print(f.read())