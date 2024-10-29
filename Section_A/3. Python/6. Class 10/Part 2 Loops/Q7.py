# Find the factorial of a number using a while loop.
# # for
# factNum = 5
# fac = 1
# for i in range(1, 6):
#     print("fac : ", fac, " i: ", i)
#     fac = fac * i

# print("final factorial of ", factNum, " is ", fac)

# while
factNum = 5
fac = 1
i = 5
while i >= 1:
    print("fac : ", fac, " i: ", i)
    fac = fac * i
    i = i - 1

print("final factorial of ", factNum, " is ", fac)