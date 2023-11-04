def add(op1, op2):
    return op1 + op2


def subtract(op1, op2):
    return op1 - op2


def multiply(op1, op2):
    return op1 * op2


def divide(op1, op2):
    return op1 / op2


while True:
    print("Choose the operation: ")
    print("1.  Addition")
    print("2.  Subtraction")
    print("3.  Multiplication")
    print("4.  Division")
    choice = int(input())

    print("Enter the 2 operands:")
    op1 = int(input("First:"))
    op2 = int(input("Second:"))

    if choice == 1:
        print(add(op1, op2))

    elif choice == 2:
        print(subtract(op1, op2))

    elif choice == 3:
        print(multiply(op1, op2))

    elif choice == 4:
        print(divide(op1, op2))

    print("Do you want to continue operation ?:(yes/no)")
    ch = input().lower()  # to change the input into lowercase
    if ch == "no":
        break


