
def convertToCelsius(f):
    c =  (f-32) * 5/9
    return c
def convertToFahrenheit(c):
    f = (9/5)*c+32
    return f

while True:
    print ("\nMENU")
    print ("1. Convert Celsius to Fahrenheit")
    print ("2. Convert Fahrenheit to Celsius")
    print ("3. Exit")

    choice = input("Enter your choice from 1-3:")

    if choice == "1":
        a = float(input("Enter temperature in Celsius: "))
        fahrenheit = convertToFahrenheit(a)
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
    elif choice == "2":
        a = float(input("Enter temperature in Fahrenheit: "))
        celsius = convertToCelsius(a)
        print(f"Temperature in Fahrenheit: {celsius:.2f}")      
    elif choice == "3": 
        print("Goodbye")
        break
    else:
        print ("Invalid Choice, Try again")