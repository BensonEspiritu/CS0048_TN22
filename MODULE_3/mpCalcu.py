
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

while True:
    print ("\nMENU")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")
    print ("5. Exit")

    choice = input("Enter your choice from 1-5:")

    if choice == "1":
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        print(f"Result:",add(a,b))
    elif choice == "2":
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        print(f"Result:",subtract(a,b))        
    elif choice == "3":
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        print(f"Result:",multiply(a,b))          
    elif choice == "4":
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        if b == 0:
            print("Cannot divide by zero")
            continue
        else:
            print(f"Result:",multiply(a,b))   
    elif choice == "5": 
        print("Goodbye")
        break
    else:
        print ("Invalid Choice, Try again")