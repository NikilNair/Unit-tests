def add(x, y):
    # print(f"Your output is {x + y}")
    return x + y


def sub(x, y):
    # print(f"Your output is {x - y}")
    return x - y


def mul(x, y):
    # print(f"Your output is {x * y}")
    return x * y


def div(x, y):
    # print(f"Your output is {x / y}")
    return x / y


inp = input("What operation would you like to perform, 'add', 'subtract', 'multiply', 'divide': ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if inp == "add":
    print(f"Your output is {add(num1, num2)}")

elif inp == "subtract":
    print(f"Your output is {sub(num1, num2)}")

elif inp == "multiply":
    print(f"Your output is {mul(num1, num2)}")

elif inp == "divide":
    print(f"Your output is {div(num1, num2)}")
