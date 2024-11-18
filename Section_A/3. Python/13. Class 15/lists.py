# Basic Level

# # Create a list of numbers from 1 to 10 and print it.
# list = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print("list -> ", list)

# for i in range(0, 10):
#     print("list[" + str(i) + "] ->", list[i])

# for num in list:
#     print(num)
    
    
    


# # Access the third element of a list [5, 10, 15, 20, 25].

# list = [5, 10, 15, 20, 25]
# print(list[2])

# # Append the number 100 to a list and print the updated list.

# list = [5, 10, 15, 20, 25]
# list.append(100)
# print(list)


# # Remove the element 20 from the list [10, 20, 30, 40].

# list = [10, 20, 30, 40]
# list.pop(1)
# print(list)

# # Find the length of the list [7, 14, 21, 28, 35].

# list = [7, 14, 21, 28, 35]
# print(len(list))

# # Use slicing to get the first three elements from [2, 4, 6, 8, 10].

# list = [2, 4, 6, 8, 10]

# slicedList = list[0:3]
# print(slicedList)

# Combine two lists [1, 2, 3] and [4, 5, 6] into a single list.

# combinedList = [1, 2, 3] + [4, 5, 6]
# print(combinedList)


# x = [4, 5, 6]
# y = x.copy()
# x.append(8)
# print("x ", x)
# print("y ", y)




# Check if the value 50 is present in the list [10, 20, 30, 40, 50].

# list = [10, 20, 30, 40, 50]

# if 50 in list:
#     print("50 is in the list.")
# else:
#     print("50 is not in the list.")

# fifty_in_list = False
# for num in list:
#     if 50 == num:
#         print("50 is in the list.")
#         fifty_in_list = True
#         break
# if fifty_in_list == False:
#     print("50 is not in the list.")

# Intermediate Level

# # Reverse the list [1, 2, 3, 4, 5] without using the reverse method.

# list = [1, 2, 3, 4, 5]
# reversedList = []
# for i in range(4, -1, -1):
#     reversedList.append(list[i])

# print(list)
# print(reversedList)




# Sort the list [34, 12, 78, 4, 56] in ascending order.

list = [34, 12, 78, 4, 56]
list.sort()
print(list)



# Replace the second element of the list [11, 22, 33, 44, 55] with 99.


# Find the index of 25 in the list [10, 15, 25, 35, 45].


# Create a new list with only even numbers from [1, 2, 3, 4, 5, 6, 7, 8].



# Use a loop to sum up all elements in the list [5, 10, 15, 20].



# Advanced Level

# Create a list comprehension that generates a list of squares for numbers 1 through 10.
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Flatten a nested list [[1, 2], [3, 4], [5, 6]] into a single list.

# Remove all duplicates from the list [10, 20, 20, 30, 40, 10, 50].
# Count how many times the number 4 appears in the list [4, 4, 3, 2, 1, 4, 5].
# Write a program to rotate a list [1, 2, 3, 4, 5] to the right by 2 positions.
# Write a program to find the maximum and minimum values in the list [23, 45, 12, 78, 34, 89].