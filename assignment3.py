#Question 1 - Declarinf the variables
Name = "King Zumah"
Age = 29
Height = 6.1
Is_student = True


#Question 2 - Write a program that prints the type of each variable you created
print("type of Name", type(Name))
print("type of Age", type(Age))
print("type of Height", type(Height))
print("type of Is_student", type(Is_student))


#Question 3 - Working with variables

x = 5
y = 2.5

# Their sum
sum_result = x + y
print("Sum:", sum_result)

# Their product
product_result = x * y
print("Product:", product_result)

# The type of the result of x + y
print("Type of x + y:", type(sum_result))

#Question 4 - Create a variable called message and assign your full name to it.
message = "Eben King"
first_name = message[:4]
print("First Name:", first_name)

#Question 5 - Create a program that asks a user to do some things

# Get two numbers from the user
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

# Perform operations
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division (float):", num1 / num2)
print("Remainder:", num1 % num2)

#Question 5 - Write a program that compares the age of two people

# Get the two ages
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))

# Compare ages
if age1 > age2:
    print("Person 1 is older.")
elif age2 > age1:
    print("Person 2 is older.")
else:
    print("Both are the same age.")

# Check if they are equal
print("Are their ages equal?", age1 == age2)
