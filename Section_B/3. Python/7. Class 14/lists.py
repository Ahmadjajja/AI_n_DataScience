# Introduction to Lists
# In lists, we can store multiple values of multiple types of data.
# In variable we can store only 1 value but in list we can store multiple values at once.



# Creating Lists

student1_name = "Ahmad"
student2_name = "Ali"
student3_name = "Ameer"

students = ["Ahmad", "Ali", "Ameer", 56, 72, 32]

# # Accessing Elements

# print(student1_name, " === ", students[0])
# print(student2_name, " === ", students[1])
# print(student3_name, " === ", students[2])

# # Negative Indexing

# print(student1_name, " === ", students[-3])
# print(student2_name, " === ", students[-2])
# print(student3_name, " === ", students[-1])

# Modifying Elements in a List

student3_name = "Amir"
students[2] = "Amir"

print("students -> ", students)

# # Slicing Lists

# # list_name[starting_inclusive_index : ending_exclusive_index: gap] 

# # ["Ahmad", "Ali", "Amir", 56, 72, 32]

# students_names_data = students[0:3:2]
# students_nums_data = students[3:]
# print(students_names_data)
# print(students_nums_data)



# Adding Elements to a List

#     append()
print("students list before appending values: ", students)
students.append(56)
students.append(42)
print("students list after appending values: ", students)
#     insert()
students.insert(2, "Azam")
print("students list after inserting value at index 2: ", students)


# Removing Elements from a List
#     remove()
students.remove(32)
print("students list after removing 32: ", students)
#     pop()
students.pop(2)
students.insert(2, "Azeem")
print("students list after removing and inserting value at index 2: ", students)
students.pop()
print("students list after removing value at last: ", students)

#     del statement

del students[1]
print("students list after removing value at last: ", students)


# Looping Through a List
#     for loop
for student in students:
    print(student)
    
# for i in range(0, len(students)):
#     print(students[i])

#     while loop

print("Looping using while loop on list")

index = 0
while index < len(students):
    print(students[index])
    index = index + 1
    
# List Methods

#     len()
print("len(students) -> ", len(students))
#     count()
print("students.count(56) -> ", students.count(56))

#     index()
print("students.index(56) -> ", students.index(56))

#     sort()
nums = [5, 4, 65, 34, 232, 4]
names = ["Zaka", "Ali", "Babu", "Ahmad"]
nums.sort()
names.sort()
print("nums after sorting -> ", nums)
print("names after sorting -> ", names)

#     reverse()

nums.reverse()
print(nums)



# Copying Lists
#     Shallow Copy (list.copy(), slicing)
#     Deep Copy (copy.deepcopy())

# List Comprehension

# Nested Lists (Multidimensional Lists)

# Common List Operations
#     Membership (in, not in)
#     Concatenation (+)
#     Repetition (*)

# Immutable Alternatives to Lists (Tuples as a comparison)