def SumFirstNnaturalNumbers(n):
    if n == 1:
        return 1
    else:
        return n + SumFirstNnaturalNumbers(n - 1)



def printStarPattern(n):
    if n == 0:
        return
    else:
        print("*" * n)
        printStarPattern(n - 1)

print(printStarPattern(5))



#! Write a python function to remove a given word from a list ad strip it at the same time.
def removeWord(l, word):
    if l == []:
        return []
    else:
        n = []
        for item in l:
            if not(item == word):
                n.append(item.strip(word))
        return n

l = ["Harry", "Soham", "Sachin", "Rahul", "S"]
print(removeWord(l, "S"))
