#Ex1
#Deciding whether the number is divisible by both 3 and 5, just 3, just 5, or neither.
def fizzbuzz(n):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


for i in range(1,21):
    fizzbuzz(i)
#output: 1,2Fizz,3,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz

#Ex2
#filter instances of int out of the list and create to the new one
mixed_list = [10, "Hello", 3.14, 20, "World", 7, 8.9]

filtered_list = [x for x in mixed_list if isinstance(x, int)]

print(filtered_list)

#output: [10, 20, 7]

#Ex3
#simple to do list to add and check exisiting elements in the list
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def show_tasks():
    if todo_list:
        print("Tasks:")
        for task in todo_list:
            print(f"- {task}")
    else:
        print("No tasks in the to-do list.")

add_task("Do laundry")
#output: "Task 'Do laundry' added to the list."
add_task("Throw out trash")
#output: "Task 'Throw out trash' added to the list."
show_tasks()
#output: "Tasks:
#- Do laundry
#- Throw out trash"

#Ex4
#changing celsius temperature into a fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures_celsius = [22, 46, 51, 76]
for temp in temperatures_celsius:
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")

#output: "22°C is 71.6°F
#46°C is 114.8°F
#51°C is 123.8°F"
