def calculate(num1, num2, op):
  """
  Performs the specified operation on two numbers.

  Args:
      num1: The first number.
      num2: The second number.
      op: The operator (+, -, *, /).

  Returns:
      The result of the operation.
  """
  if op == '+':
    return num1 + num2
  elif op == '-':
    return num1 - num2
  elif op == '*':
    return num1 * num2
  elif op == '/':
    if num2 == 0:
      print("Error: Division by zero!")
      return None  # Indicate error
    else:
      return num1 / num2
  else:
    print("Invalid operator!")
    return None  # Indicate error

def main():
  """
  Prompts user for input and performs calculations.
  """
  while True:
    try:
      num1 = float(input("Enter first number: "))
      op = input("Enter operator (+, -, *, /): ")
      num2 = float(input("Enter second number: "))

      result = calculate(num1, num2, op)

      if result is not None:
        print("Result: " + str(num1) + " " + op + " " + str(num2) + " = " + str(result))

      # Ask if user wants to continue
      choice = input("Do you want to perform another calculation? (y/n): ")
      if choice.lower() != 'y':
        break

    except ValueError:
      print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
  main()
