def calc():
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == '+': print(a + b)
    elif op == '-': print(a - b)
    elif op == '*': print(a * b)
    elif op == '/': 
        if b != 0: print(a / b)
        else: print("Error! Division by zero.")
    else: print("Invalid operator")
calc()