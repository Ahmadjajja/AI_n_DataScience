# Write a program to calculate the sum of all numbers between 1 and 100.

# while loop
i = 2
sum = 0
while i <= 99:
    sum = sum + i
    print("sum: ", sum, " i: ", i)
    i = i + 1

print(sum)

# for loop
sum = 0

for i in range(2, 100):
    sum = sum + i
    print("sum: ", sum, " i: ", i)
    
print(sum)

