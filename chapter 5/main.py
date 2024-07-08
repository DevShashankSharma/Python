
# #! DICTIONARY

# a = {
#     "name": "Alex",
#     "age": 20,
#     "city": "London",
#     "languages": ["Python", "Java", "C++"],
#     9: "hello",
# }

# print(a["name"],type(a))
# print(a.items())
# print(a.keys())
# print(a.values())
# print(a.get("name"))
# print(a.get("city"))
# print(a.get("country", "India")) 

# a["country"] = "India"
# print(a)

# a.update({"country": "India"})
# print(a)

# a.pop("city")
# print(a)

# a.popitem()
# print(a)

# a.clear()
# print(a)


#! SETS
a={1,2,3,4,5,"Alex"}

e = set()  #empty set  ----> Don't use e = {} as it will be a dictionary
e.add(1)
e.add(2)
e.add(3)
e.add(4)
e.add(5)

print(a)
print(e)

# operations on sets
e.remove(3)

