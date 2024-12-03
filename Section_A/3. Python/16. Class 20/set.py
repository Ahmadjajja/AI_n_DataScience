# Set
    # 4 main points: mutable itself, unique elements, unordered elements, and immutable elements

# # way-1 to create a set
# nums = {1, 4, 5, 8, 10, 4}
# print("nums set: ", nums)

# # way-2 to create a set
# numbers = set([1, 4, 5, 8, 10, 4])
# print("Numbers set: ", numbers)

# if 6 in numbers:
#     print("number found!")























# Set Methods
# 1. Adding and Removing Elements

    # add(): Adds an element to the set.
# print("number in set : ", 10 in numbers)

    # remove(): Removes an element. Raises an error if the element does not exist.
# numbers.remove(11)

    # discard(): Removes an element but does not raise an error if the element is absent.
# numbers.discard(11)

    # pop(): Removes a random element.
# numbers.pop()
# numbers.pop()

# print("Numbers set after pop: ", numbers)
    
    # clear(): Removes all elements.
# numbers.clear()

# print("Numbers set after pop: ", numbers)
    
    
    
    
    
    
    
    

# 2. Set Operations
    # union() or |: Combines two sets (all unique elements from both).
    
setList1 = set([9])
setList2 = set([0, 12, 6, 20, 1, (9, 7), 10])

print(setList1 | setList2)
print(setList1.union(setList2))

    # intersection() or &: Returns common elements.
    
print(setList1 & setList2) # {6, 9}
print(setList1.intersection(setList2)) # {6, 9}

    
    # difference() or -: Elements in the first set but not in the second.
    
print(setList1 - setList2) # {2, 3, 4, 5}
print(setList1.difference(setList2)) # {2, 3, 4, 5}
    
    
    # symmetric_difference() or ^: Elements in either set but not in both.
    
print(setList1 ^ setList2) # {2, 3, 4, 5, 0, 12, 20, 1, 7, 10}
print(setList1.symmetric_difference(setList2)) # {2, 3, 4, 5}


# 3. Subset and Superset
    # issubset(): Checks if all elements of a set are in another.
    
print(setList1.issubset(setList2))
    
    # issuperset(): Checks if a set contains all elements of another.
    
print(setList2.issuperset(setList1))

    # isdisjoint(): Checks if two sets have no elements in common.
    
print(setList2.isdisjoint(setList1))

# 4. Copying Sets
    # copy(): Creates a shallow copy.
setList3 = setList2.copy()