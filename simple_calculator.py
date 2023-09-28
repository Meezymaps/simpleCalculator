import math
import os

# Function to write an equation to the file
def write_equation_to_file(equation):

    with open('equations.txt', 'a') as file:
        file.write(equation + '\n')
        

# Function to perform the calculation based on the operator
def calculate(num1, num2, operator):

    if operator == '+':
        return math.fadd(num1, num2)
    elif operator == '-':
        return math.fsub(num1, num2)
    elif operator == '*':
        return math.fmul(num1, num2)
    elif operator == '/':
        if num2 != 0:
            return math.fdiv(num1, num2)
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Error: Invalid operator"

# Function to process an equation entered interactively
def process_equation(num1, num2, operator):

    try:
        num1 = float(num1)
        num2 = float(num2)
        result = calculate(num1, num2, operator)
        print(f"{num1} {operator} {num2} = {result}")

        equation = f"{num1} {operator} {num2} = {result}"
        write_equation_to_file(equation)
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to process equations from a file
def process_equations_from_file(filename):

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            equations = file.readlines()
            for equation in equations:
                equation = equation.strip()
                equation_parts = equation.split()
                if len(equation_parts) == 3:
                    num1, operator, num2 = equation_parts
                    process_equation(num1, num2, operator)
                else:
                    print("Error: Invalid equation format in the file")
    else:
        print("Error: File not found.")

# Function to clear the calculator display
def clear():

    # Clear the display
    

def main():

    while True:
        choice = input("Choose an option:\n1. Enter two numbers and an operator\n2. Read equations from a file\n3. Clear the display\nEnter your choice (1, 2, or 3): ")

        if choice == '1':
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            operator = input("Enter the operator (+, -, *, /): ")
            process_equation(num1, num2, operator)
        elif choice == '2':
            filename = input("Enter the name of the file: ")
            process_equations_from_file(filename)
        elif choice == '3':
            clear()
        else:
            print("Error: Invalid choice. Please enter either 1, 2, or 3.")

        choice = input("Do you want to perform another calculation? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == '__main__':
    if not os.path.exists('equations.txt'):
        open('equations.txt', 'w').close()

    main()
