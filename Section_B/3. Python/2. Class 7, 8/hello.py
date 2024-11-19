# 3. Basic Operations
# Arithmetic operations
#           There are different types of arithmatic operations:

# # +, -, /, //, *, **, %
# num1 = 5
# num2 = 2
# print("num1 + num2 : ", num1 + num2)
# print("num1 - num2 : ", num1 - num2)
# print("num1 / num2 : ", num1 / num2)
# print("num1 // num2 : ", num1 // num2)
# print("num1 * num2 : ", num1 * num2)
# print("num1 ** num2 : ", num1 ** num2)
# print("num1 % num2 : ", num1 % num2)


# # #                    String operations (concatenation, repetition)
#                    Input/output: print(), input()
# firstName = input("Enter first name : ")
# secondName = input("Enter second name : ")
# fullName = firstName + " " + secondName + " "
# print("fullname : ", fullName * 5)




# 4. Control Structures

# #                    Conditional statements: if, else, elif
# marks = int(input("Enter your marks & know your grade: "))

# # 80+ (A+), 70+ (A), 60+ (B), 50+ (C), 40+ (D), < 40 (fail)
# if marks >= 80:
#     print("He got A+ grade")
# elif marks >= 70:
#     print("He got A grade")
# elif marks >= 60:
#     print("He got B grade")
# elif marks >= 50:
#     print("He got C grade")
# elif marks >= 40:
#     print("He got D grade")
# else:
#     print("He failed the subject")

    



# #                    Logical operators: and, or, not

# # and operator
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# # or operator
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# # not operator
# not True = False
# not False = True


# Comparison Operator
# >, <, >=, <=, ==, ===(Checks both values & types), !=


#                    Loops: for, while

# for i in range(0, 10):
#     print("Hello World!! ", i)

marks = 1000
print("start...")
while marks > 0:
    print("marks : ", marks)
    if marks == 100:
        marks = marks // 10
        print("continue statement occured!!")
        continue
    marks = marks // 10
print("end...")



#                    Loop control: break, continue, pass