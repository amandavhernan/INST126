import math 

# this program makes a calculator that can add, subtract, multiply, divide, take the square root of any number, raise a number to the power of 2 or 3, and take the natural log of any number.

check = True
while(check != False): 

    print("Select an operation to perform (1-8): ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Raise to the Power of 2")
    print("7. Raise to the Power of 3")
    print("8. Take the natural logarithm")

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
        
    elif operation == "7": 
    # perform raise to the power of 3
        num = int(input("Enter number: "))
        print("The result is " + str(pow(num, 3)))
        
    elif operation == "8": 
    # perform to take the natural log of a number
        num = int(input("Enter number: "))
        print("The result is " + str(math.log(num)))
    
    elif operation == "quit": 
        check = False

    else:
        print("Invalid Entry. Please enter a value between 1-8 to choose an operation.")
