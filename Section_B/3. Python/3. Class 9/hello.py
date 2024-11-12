# 3 method of writing variable name 
# 1. Underscore b/w words(work as a space) -> year_to_check
# 2. Camel Case (first ch of 1st word is small and first ch of later words is capital) -> yearToCheck
# 2. Pascal Case (first ch of all words is capital) -> YearToCheck

# Part 1: Conditional Statements (20 Questions)

# # Write a program that checks if a given number is positive, negative, or zero.

# num = 5
# if num > 0:
#     print(num, " is +ve number")
# elif num < 0:
#     print(num, " is -ve number")
# else:
#     print(num, " is ZERO")


# # Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

# num = int(input("Enter user's age: "))
# if num < 15:
#     print("User is Minor")
# elif num < 40:
#     print("User is Adult")
# else:
#     print("Senior Citizen")



# # Write a program that checks if a given year is a leap year.
# year_to_check = int(input("Enter year: "))

# # check whether this year is leap or not


# if year_to_check % 4 == 0:
    
#     if year_to_check % 100 == 0:
        
#         if year_to_check % 400:
#             print("Leap Year")
#         else:
#             print("Not Leap Year")
            
#     else:
#         print("Leap Year")

# else:
#     print("Not Leap Year")




# Take an integer and check if it’s even or odd.



# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).


# # Write a program to find the largest of two numbers.

# num1 = 4
# num2 = 5
# if num1 > num2:
#     print(num1, ' is greater number')
# elif num1 == num2:
#     print(num1, " = ", num2)
# else:
#     print(num2, ' is greater number')

name = "Ahmad"
print(name[::-1])


# # Write a program to find the largest of three numbers.

# num1, num2, num3 = int(input("Enter n1: ")), int(input("Enter n2: ")), int(input("Enter n3: "))

# if num1 >= num2 and num1 >= num3:
#     print(num1, " is greater number.")
# elif num2 >= num1 and num2 >= num3:
#     print(num2, " is greater number.")
# else:
#     print(num3, " is greater number.")
    
        






# Create a program that checks if a given string is a palindrome.

# str = input("Enter a string: ")

# start_index = 0
# end_index = len(str) - 1

# while start_index < end_index:
#     if str[start_index] != str[end_index]:
#         print(str + " is not palindrome")
#         break
#     start_index = start_index + 1
#     end_index = end_index - 1

# if end_index <= start_index:
#     print(str + " is palindrome")
    
    


# Take three sides of a triangle as input and check if they form a valid triangle.

# Write a program to determine if a given character is a vowel or consonant.


# Check if a given number is a multiple of both 3 and 5.

# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
# 
# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

# Check if a year input by the user is a century year.

# Write a program to check if a number is within a specified range.

# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

# Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

# Take a user’s score and determine if they pass or fail (pass if 50 or above).

# Check if a string input is uppercase, lowercase, or a mix.

# Create a program that evaluates if an inputted number is prime.
