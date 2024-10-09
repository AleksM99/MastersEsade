#Ex1

def fizzbuzz(n):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


for i in range(1,20):
    fizzbuzz(i)


#Ex2
mixed_list = [10, "Hello", 3.14, 20, "World", 7, 8.9]

filtered_list = [x for x in mixed_list if isinstance(x, int)]

print(filtered_list)


#Ex3
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
add_task("Throw out trash")
show_tasks()

#Ex4

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures_celsius = [22, 46, 51, 76]
for temp in temperatures_celsius:
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")