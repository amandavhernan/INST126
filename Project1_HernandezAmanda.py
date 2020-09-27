import math 

# this program makes a calculator that can add, subtract, multiply, divide, take the square root of any number, and raise a number to the power of 2.

check = True
while(check != False): 

    print("Select an operation to perform (1-6): ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Raise to Power of 2")

    operation = input()

    if operation == "1":
    # perform addition
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The sum is " + str(int(num1) + int(num2)))

    elif operation == "2": 
    # perform subtraction
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The difference is " + str(int(num1) - int(num2)))

    elif operation == "3":
    # perform multiplication
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The product is " + str(int(num1) * int(num2)))

    elif operation == "4": 
    # perform division
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The result is " + str(int(num1) / int(num2)))

    elif operation == "5": 
    # perform square root
        num = int(input("Enter number: "))
        print("The square root is " + str(math.sqrt(num)))

    elif operation == "6": 
    # perform raise to the power of 2
        num = int(input("Enter number: "))
        print("The result is " + str(pow(num, 2)))
    
    elif operation == "quit": 
        check = False

    else:
        print("Invalid Entry. Please enter a value between 1-6 to choose an operation.")
