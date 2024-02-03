# This is a simple Python script demonstrating exception handling

def divide_numbers(x, y):
    try:
        result = x / y
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except TypeError:
        print("Error: Please provide valid numeric inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division operation completed successfully.")
    finally:
        print("This block always executes, regardless of whether there was an exception.")

# Example usage
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    divide_numbers(num1, num2)
except ValueError:
    print("Error: Please enter valid numeric inputs.")
except Exception as e:
    print(f"An unexpected error occurred during input processing: {e}")
