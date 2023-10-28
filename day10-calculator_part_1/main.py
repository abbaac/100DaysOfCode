from art import logo
from replit import clear
from art import logo

def add(num1, num2):
    return num1 + num2 

def sub(num1, num2):
    return num1 - num2 

def mul(num1, num2):
    return num1 * num2 

def div(num1, num2):
    return num1 / num2 

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

def next_choice():
    for i in operations:
        print(i)
    operation = input("Select from above the operation you wish to do on these number: ")
    num = float(input("What's the next number: "))
    return operation, num

def calculator():
    print(logo)
    num1 = float(input("Input the first number: "))

    resume = True
    while resume:
        operate, next_num = next_choice()
        answer = operations[operate](num1, next_num)
        print(f"{num1} {operate} {next_num} = {answer}")

        choice = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: " ).lower()
        if choice == "n":
            resume = False
            clear()                        
            calculator()

        else:
            num1 = answer

calculator()

