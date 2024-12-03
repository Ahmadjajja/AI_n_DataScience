# Changing Case

# first_name = "Ahmad"
# print(first_name.lower())
# print(first_name.upper())

# Dictionaries



# students = [
#     {
#     "name": "hamza",
#     "id": "1dff42dd",
#     "age": "17",
#     "education": "Intermediate",
#     "programming_skills": "Python"
#     },
#     {
#     "name": "Ali",
#     "id": "1dfhgf2dd",
#     "age": "21",
#     "education": "Undergraduate",
#     "programming_skills": "Python, Java, C++"
#     }
# ]

# for student in students:
#     print("_______________________")
#     print("_______________________")
#     print(student)


# person = {
#     "name": "hamza",
#     "age": "17",
#     "education": "Intermediate",
#     "programming_skills": "Python"
# }


# print(person["education"])
# print(person["name"])

# Store 5 table in dictionary

five_table = {
    (1, 2): 5,
    2: 10,
    3: 15,
    4: 20,
    (5): 25,
    6: 30,
    7: 35,
    8: 40,
    9: 45,
    10: 50,
}

# five_table[11] = 55
# print(five_table[11])


# print(five_table)
# del five_table[9]
# five_table[(1, 2)] = 45
# print(five_table)

print(five_table.keys())
print(five_table.values())

for key in five_table.keys(): 
    print(key, " : ", five_table[key], ",")


for value in five_table.values():
    print("value -> ", value)