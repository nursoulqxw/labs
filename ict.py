num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
operation= input("Perform operations with these numbers (+, -, *, /) :" )

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error: Division by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)

# 2

while True:
    num1 = float(input("Enter the first number (or 'q' to quit): "))
    if num1 == 'q':
        break
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation : ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            result = "Error: division by zero"
        else:
            result = num1 / num2
    else:
        result = "Invalid operation"

    print("Result:", result)
#3
for i in range(1, 21):
    print(i)
#4
numbers = list(range(1, 11))
for number in numbers:
    print(number ** 2)

#5
breads = ["white", "whole grain"]
meats = ["turkey", "ham"]
vegetables = ["lettuce", "tomato"]
sauces = ["mayo", "mustard"]

for bread in breads:
    for meat in meats:
        for vegetable in vegetables:
            for sauce in sauces:
                print(f"Sandwich with {bread} bread, {meat}, {vegetable}, and {sauce}")

#6
sum_even = sum(i for i in range(1,101) if i%2==0)
sum_odd = sum(i for i in range(1,101) if i%2!=0)

print("Sum of even nums: ", sum_even)
print("Sum of odd nums: ", sum_odd)
#7
num = int(input("Enter a number to find its factorial: "))
factorial = 1

for i in range(1, num + 1):
    factorial *=i

print(f"The factorial of {num} is {factorial}")