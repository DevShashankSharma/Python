name = input("Enter your name: ")
print(f"Good Afternoon {name}")

letter = """
Dear <|name|>,
Greetings from ABC coding house. I am happy to tell you that you are selected
<|date|>
""" 
letter = letter.replace("<|name|>", "Alex").replace("<|date|>", "29/09/2022")
print(letter)

#! wap to detect double space in string

name = "My name  is Alex"
print(name.find("  "))
print(name.replace("  ", " "))


#!Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry, this python course is nice. Thanks!"
newletter = "Dear Harry,\n\tthis python course is nice. \nThanks!"
print(newletter)