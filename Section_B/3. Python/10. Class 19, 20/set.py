# Set
    # 1. Unique elements
    # 2. Un-ordered elements
    # 3. Im-mutable elements
    # 4. it-self mutable

# method-1 to define set
setElements = set([2, 3, 4, (5, 5, 5), 3, 2]) # empty set

print("setElements : ", setElements)

# method-2 to define set
setElements2 = {2, 3, 4, 5, 5, 5, 3, 2} # empty dictionary

print("setElements2 : ", setElements2)



















# # Set Methods
# # 1. Adding and Removing Elements

#     # add(): Adds an element to the set.
# setElements.add(20)
# print(setElements)

#     # remove(): Removes an element. Raises an error if the element does not exist.
# # setElements.remove(200)
# # print(setElements)

#     # discard(): Removes an element but does not raise an error if the element is absent.
# setElements.discard(200)
# print(setElements)

#     # pop(): Removes a random element.
# print(setElements.pop())
# print(setElements)
    
#     # clear(): Removes all elements.
# setElements.clear()
# print(setElements)
    
    
    
    
    
    
    
    
    

# 2. Set Operations
    # union() or |: Combines two sets (all unique elements from both).
print({1, 2, 3, 4, 5}.union({3, 4, 5, 6, 7}))
print({1, 2, 3, 4, 5} | {3, 4, 5, 6, 7})


    # intersection() or &: Returns common elements.
print({1, 2, 3, 4, 5} & {3, 4, 5, 6, 7})
    
    # difference() or -: Elements in the first set but not in the second.
print({1, 2, 3, 4, 5} - {3, 4, 5, 6, 7})


    # symmetric_difference() or ^: Elements in either set but not in both.
print({1, 2, 3, 4, 5} ^ {3, 4, 5, 6, 7})
    
    
    
    
    
    


# 3. Subset and Superset
    # issubset(): Checks if all elements of a set are in another.
    
    # issuperset(): Checks if a set contains all elements of another.

    # isdisjoint(): Checks if two sets have no elements in common.

# 4. Copying Sets
    # copy(): Creates a shallow copy.
print("setElements -> ", setElements)
setElements3 = setElements.copy()

setElements3.remove(4)

print("setElements3 -> ", setElements3)
print("setElements -> ", setElements)

