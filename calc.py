# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs"
#    formated_f_name = f_name.title()
#    formated_l_name = l_name.title()
#    return f":Result {formated_f_name} {formated_l_name}"
#
# print(format_name("Traybuns", "Gobum"))
#
#
#
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True  #
#     else:
#         return False
#
#
# print(is_leap(2400))
# print(is_leap(1989))
# print(is_leap(2000))
# print(is_leap(2100))
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2 if n2 != 0 else "Error: Division by zero"


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        if operation_symbol in operations:
            answer = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            print("Invalid operation. Please try again.")
            continue

        choice = input(f"Type 'Y' to continue calculating with {answer}, or type 'N' to start over: ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 5)
            calculator()  # Restart the calculator


calculator()


