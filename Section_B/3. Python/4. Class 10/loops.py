# Part 2: Loops (20 Questions)

# # Print numbers from 1 to 20 using a for loop.

# for i in range(1, 21):
#     print(i)
    

# # Use a for loop to print even numbers from 1 to 50.

# num = 1
# while num <= 50:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)
        
# for i in range(2, 51, 2):
#     print(i)

# # Write a program to calculate the sum of all numbers between 1 and 100.

# sum = 0

# for i in range(1, 101):
#     sum = sum + i

# print("Sum -> ", sum)

# Print the multiplication table of a given number.

# Print all odd numbers between 1 and 100 using a loop.

# Use a for loop to print each character of a string.
"Ahmad"

# Find the factorial of a number using a while loop.
# 6 -> 6 * 5 * 4 * 3 * 2 * 1

# Use a for loop to print numbers from 10 down to 1.

# Write a program to print the first 10 Fibonacci numbers.

# 0, 1, 1, 2, 3, 5, ......

# Use a loop to count the number of digits in an integer.

# Print the reverse of a given number.

# Print all prime numbers between 1 and 50.

for num in range(2, 50):
    isPrimeNumber = True

    for i in range(2, num):
        if num % i == 0:
            isPrimeNumber = False
            break
            
    if isPrimeNumber:
        print(num, " is prime number")



# Use nested loops to print a pyramid pattern of *.
# Write a program that breaks the loop when a certain condition is met.
# Print the sum of even and odd numbers separately up to a given number.

# # Create a program to calculate the sum of the digits of an inputted integer.
# num = abs(int(input("Enter any number: "))) # 505 % 10 = right digit(5),  505 / 10 = left digit (5)
# sum = 0

# while num > 0:
#     sum += num % 10
#     num = num / 10

# print("Sum : ", int(sum))



# # Write a program that continues to ask for a number until the correct number is guessed.
# number = 50
# correct_number_found = False

# while not correct_number_found:
#     inputNum = int(input("Enter a number: "))
#     if inputNum == number:
#         correct_number_found = True
#         print("Congrats. U hv guessed the correct number!!!")
#     else:
#         print("U hit a wrong number")

# Use a loop to print numbers in reverse order within a given range.



# # Use a for loop to print the square of each number from 1 to 10.
# for i in range(1, 11):
#     print(i*i)



# # Create a program that simulates a countdown timer starting from a given number down to zero.

# for i in range(50, -1, -1): # i = 50 + (-1) -> 49
#     print(i)