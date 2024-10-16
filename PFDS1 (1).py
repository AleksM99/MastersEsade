
# Ex. 1:
print("Hello, Python!")

# Ex. 2:
a = 12
b = 98
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

#Ex. 3:
name = "Aleks"
print(f"Hello, {name}!")

#Ex. 4:
universities = ["StGallen", "MIT", "Esade", "UAB", "SGH"]
print("Universities list:", universities)
print("First university:", universities[0])
print("Last university:", universities[-1])

# Ex. 5:
student = {
    "name": "Aleks",
    "age": 24,
    "grade": 7
}
for key, value in student.items():
    print(f"{key}: {value}")

# Ex. 6:
coordinates = (50, 109)
print("Coordinates tuple:", coordinates)
print("X:", coordinates[0])
print("Y:", coordinates[1])

# Ex. 7:
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.add("red")  # Attempt to add a duplicate
print("Colors set:", colors)
colors.remove("green")

light_colors = {"white", "pink"}
all_colors = colors.union(light_colors)
print("Merged set:", all_colors)

# Ex. 8:
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Ex. 9:
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Ex. 10:
count = 1
while count <= 5:
    print(count)
    count += 1

# Ex. 11

grade = input("Enter a grade (A, B, C, D, F): ").upper()
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

# Ex. 12
def greet(name):
    print(f"Hello, {name}!")

greet("Aleks")

# Ex. 13:
def square(number):
    return number ** 2

print("Square of 17:", square(17))
print("Square of 909:", square(909))

# Ex. 14:
def multiply(a, b=1):
    return a * b

print("Multiply 3 and 4:", multiply(3, 4))
print("Multiply 5:", multiply(5))

# Ex. 15:
numbers = list(range(1, 11))
squares = [num ** 2 for num in numbers]
print("Squares:", squares)

# Ex. 16:
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

# Ex 17:

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

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(f"The result is: {result}")

