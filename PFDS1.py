# PFDS1.py - Python Fundamental Exercises

# Exercise 1: Basic print statement
# This prints a basic "Hello, Python!" message.
print("Hello, Python!")

# Exercise 2: Sum of two numbers
# This calculates the sum of two integers a and b.
a = 12
b = 98
print("Sum:", a + b)
# Output: Sum: 110

# Exercise 3: Check if a number is even or odd
# Takes an integer and checks if it is even or odd.
num = 13
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
# Output: The number is odd.

# Exercise 4: Check if a number is positive, negative, or zero
# Takes an integer as input and checks if it's positive, negative, or zero.
number = -7
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
# Output: The number is negative.

# Exercise 5: Print each number in a list
# Iterates through a list and prints each number.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# Output: 1, 2, 3, 4, 5

# Exercise 6: While loop example
# Prints numbers 1 to 5 using a while loop.
count = 1
while count <= 5:
    print(count)
    count += 1
# Output: 1, 2, 3, 4, 5

# Exercise 7: Matching grades with messages
# Takes a letter grade and matches it with a corresponding message.
grade = "A"
match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Good job!")
    case "C":
        print("Fair.")
    case "D":
        print("Needs improvement.")
    case "F":
        print("Failing.")
    case _:
        print("Invalid grade entered.")
# Output: Excellent!

# Exercise 8: Function to greet a user by name
# Takes a name as input and prints a greeting message.
def greet(name):
    print(f"Hello, {name}!")

greet("Aleks")
# Output: Hello, Aleks!

# Exercise 9: Function to calculate the square of a number
# Takes a number as input and returns its square.
def square(number):
    return number ** 2

print("Square of 17:", square(17))
# Output: Square of 17: 289
print("Square of 909:", square(909))
# Output: Square of 909: 826281

# Exercise 10: Function with default arguments
# Multiplies two numbers. The second number has a default value of 1.
def multiply(a, b=1):
    return a * b

print("Multiply 3 and 4:", multiply(3, 4))
# Output: Multiply 3 and 4: 12
print("Multiply 5:", multiply(5))
# Output: Multiply 5: 5

# Exercise 11: List comprehension to create a list of squares
# Generates a list of squares from numbers 1 to 10.
numbers = list(range(1, 11))
squares = [num ** 2 for num in numbers]
print("Squares:", squares)
# Output: Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercise 12: Dictionary and average grade calculation
# Stores student grades in a dictionary and calculates the average for each student.
students_grades = {
    "Alice": [85, 90, 78],
    "Bob": [75, 80, 72],
    "Charlie": [95, 100, 92]
}

def print_average_grades(students):
    for student, grades in students.items():
        average = sum(grades) / len(grades)
        print(f"{student}'s average grade: {average:.2f}")

print_average_grades(students_grades)
# Output: Alice's average grade: 84.33, Bob's average grade: 75.67, Charlie's average grade: 95.67

# Exercise 13: Basic calculator function
# Takes two numbers and an operator (+, -, *, /) as input and performs the corresponding operation.
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"

num1 = 25
num2 = 5
operator = "+"
result = calculate(num1, num2, operator)
print(f"The result is: {result}")
# Output: The result is: 30
"""
