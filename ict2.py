#1
temp = float(input("Enter the temperature value: "))
direction = input("Enter 'c' to convert from Celsius to Fahrenheit or 'f' to convert from Fahrenheit to Celsius: ").strip().lower()

if direction == 'c':
    converted_temp = temp * 9/5 + 32
    print(f"{temp}°C is {converted_temp:.2f}°F.")
elif direction == 'f':
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is {converted_temp:.2f}°C.")
else:
    print("invalid input. please enter 'c' or 'f'.")
#2
import random

target = random.randint(1, 100)
while True:
    guess = input("Guess the number (or type 'q' to quit): ")
    if guess.lower() == 'q':
        print("Game exited.")
        break
    guess = int(guess)
    if guess > target:
        print("too high!")
    elif guess < target:
        print("too low!")
    else:
        print("congrats! you guessed it!.")
        break

#3
n = int(input("Enter the number of terms for the Fibonacci sequence: "))
if n <= 0:
    print("please enter a positive integer.")
else:
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
#4
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print(f"Number of unique words: {len(unique_words)}")

#5
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#6
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

while True:
    print("\nMenu:\n1. Add\n2. Subtract\n3. Multiply\n4. Exit")
    choice = input("choose an option: ")
    if choice == '4':
        print("exiting program.")
        break
    elif choice in {'1', '2', '3'}:
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))
        if choice == '1':
            print(f"result: {add(x, y)}")
        elif choice == '2':
            print(f"result: {subtract(x, y)}")
        elif choice == '3':
            print(f"result: {multiply(x, y)}")
    else:
        print("invalid selection. try again.")

#7
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 24.9:
    category = "normal weight"
elif 25 <= bmi < 29.9:
    category = "overweight"
else:
    category = "obesity"
print(f"Your BMI is {bmi:.2f}. Category: {category}.")

#8
to_do_list = []

while True:
    print("\nTo-Do List Manager:\n1. Add item\n2. View items\n3. Remove item\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        item = input("Enter a new to-do item: ")
        to_do_list.append(item)
        print("item added.")
    elif choice == '2':
        if to_do_list:
            print("To-Do List:")
            for i, item in enumerate(to_do_list, 1):
                print(f"{i}. {item}")
        else:
            print("the to-do list is empty.")
    elif choice == '3':
        index = int(input("Enter the number of the item to remove: ")) - 1
        if 0 <= index < len(to_do_list):
            removed_item = to_do_list.pop(index)
            print(f"removed item: {removed_item}")
        else:
            print("Invalid index.")
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("invalid selection. try again.")

#9
num = int(input("Enter a number for the multiplication table: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

#10
numbers = [x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0]
print("Numbers divisible by both 3 and 5:", numbers)

