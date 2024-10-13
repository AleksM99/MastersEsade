"""
# Lesson2.py - Python Exercises

# Exercise 1: FizzBuzz
# This function checks whether a number is divisible by both 3 and 5, just by 3, just by 5, or by neither.
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Loop through numbers from 1 to 20 and apply the fizzbuzz function
for i in range(1, 21):
    fizzbuzz(i)
# Output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz

# Exercise 2: Filter integers from a list
# This creates a new list containing only the integer values from a mixed list.
mixed_list = [10, "Hello", 3.14, 20, "World", 7, 8.9]

# Using list comprehension to filter out integers
filtered_list = [x for x in mixed_list if isinstance(x, int)]

print(filtered_list)
# Output: [10, 20, 7]

# Exercise 3: Simple To-Do List
# This creates a to-do list, allows adding tasks, and displaying all tasks in the list.
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

# Function to display tasks
def show_tasks():
    if todo_list:
        print("Tasks:")
        for task in todo_list:
            print(f"- {task}")
    else:
        print("No tasks in the to-do list.")

# Add tasks and display them
add_task("Do laundry")
# Output: "Task 'Do laundry' added to the list."
add_task("Throw out trash")
# Output: "Task 'Throw out trash' added to the list."
show_tasks()
# Output: Tasks:
# - Do laundry
# - Throw out trash

# Exercise 4: Celsius to Fahrenheit Conversion
# Converts a temperature from Celsius to Fahrenheit using the formula (Celsius * 9/5) + 32
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures_celsius = [22, 46, 51, 76]

# Loop through temperatures in Celsius and convert them to Fahrenheit
for temp in temperatures_celsius:
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
# Output: 22°C is 71.6°F
#         46°C is 114.8°F
#         51°C is 123.8°F
#         76°C is 168.8°F
"""
