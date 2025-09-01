# Function for mathematical operations

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b


previous_answer = 0
use_previous = False   # flag to check if we continue with previous result

while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulus")
    print("6.Exponent")

    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):

        # if user wants to continue, first number = previous answer
        if use_previous:
            num1 = previous_answer
            print(f"Using previous answer: {num1}")
        else:
            num1 = float(input("Enter first number: "))

        num2 = float(input("Enter second number: "))

        if choice == '1':
            previous_answer = addition(num1, num2)
            print(num1, "+", num2, "=", previous_answer)

        elif choice == '2':
            previous_answer = subtraction(num1, num2)
            print(num1, "-", num2, "=", previous_answer)

        elif choice == '3':
            previous_answer = multiplication(num1, num2)
            print(num1, "*", num2, "=", previous_answer)

        elif choice == '4':
            previous_answer = division(num1, num2)
            print(num1, "/", num2, "=", previous_answer)

        elif choice == '5':
            previous_answer = modulus(num1, num2)
            print(num1, "%", num2, "=", previous_answer)

        elif choice == '6':
            previous_answer = exponent(num1, num2)
            print(num1, "^", num2, "=", previous_answer)
    
    else:
        print("Invalid input")
        break

    # ask if user wants to continue with previous answer
    choice = input("Do you want to continue with previous answer? (yes/no): ").lower()
    if choice == "yes":
        use_previous = True
    else:
        use_previous = False
        break
