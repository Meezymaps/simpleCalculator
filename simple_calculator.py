import os

# Function to write an equation to the file
def write_equation_to_file(equation):

    with open('equations.txt', 'a') as file:
        file.write(equation + '\n')

# Function to perform the calculation based on the operator
def calculate(num1, num2, operator):

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
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
        print("An error occurred:", str(e))

# Function to process equations from a file
def process_equations_from_file(filename):

    try:
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
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    
    while True:
        choice = input("Choose an option:\n1. Enter two numbers and an operator\n2. Read equations from a file\nEnter your choice (1 or 2): ")

        if choice == '1':
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            operator = input("Enter the operator (+, -, *, /): ")
            process_equation(num1, num2, operator)
        elif choice == '2':
            filename = input("Enter the name of the file: ")
            process_equations_from_file(filename)
        else:
            print("Error: Invalid choice. Please enter either 1 or 2.")

        choice = input("Do you want to perform another calculation? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == '__main__':
    if not os.path.exists('equations.txt'):
        open('equations.txt', 'w').close()

    main()
