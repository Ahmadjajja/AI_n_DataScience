# Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

age = int(input("Enter your age : "))

if age < 18:
    print("U r minor.")
elif age >= 18 and age <= 50:
    print("U r adult.")
else:
    print("U r senior citizen.")
    
    