# Write a function to calculate the area of a circle given its radius.


# function definition
def area_of_circle(r = 3):
    pi = 3.14
    def displayPi(p):
        print(p)
    displayPi(pi)
        
    return 2 * pi * (r ** 2)

# taking value from user
radius = float(input("Enter radius of a circle: "))

# function calling
print("area_of_circle(radius) -> ", area_of_circle(radius))
    
    

# # create a function to calculate the sum of 3 numbers

# def sum(num1, num2 = 5, num3 = 10):
    
    
    
#     return num1 + num2 + num3

# n1 = int(input("Enter num1: "))
# n2 = int(input("Enter num2: "))
# # n3 = int(input("Enter num3: "))

# print(sum(n1, n2))


