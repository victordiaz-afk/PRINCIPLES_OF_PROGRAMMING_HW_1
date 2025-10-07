print("This program adds and subtracts two numbers.")
num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

sum = float(num_1) + float(num_2)
print("The sum of",num_1, "and", num_2, "is", sum)
subtraction = float(num_1) - float(num_2)
print("The subtraction of", num_1, "and", num_2, "is", subtraction, '\n')


print("This program multiplies and divides two numbers.")
num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

multiplication = float(num_1) * float(num_2)
print("The multiplication of", num_1, "and", num_2, "is", multiplication)
if float(num_2) != 0:
    division = float(num_1) / float(num_2)
    print("The division of", num_1, "and", num_2, "is", division)
else:
    print("Division by zero is not allowed.")


 
