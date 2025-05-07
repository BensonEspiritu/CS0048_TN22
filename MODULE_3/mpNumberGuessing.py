import random
counter = 0


def number_guessing_game():
        print("Generating a number from 1-100...")
        random_number = random.randint(1,100)
        while True:
            user_number = int(input("Guess the number 1-100: "))
            global counter
            counter += 1
            if user_number == random_number:
                print(f"\nYou guessed the number in {counter} attempts")
                break
            elif user_number < random_number:
                print("\nToo low")
                continue
            elif user_number > random_number:
                print("\nToo high")
            else:
                print("Invalid number")
                continue
while True:
    print ("\nMENU")
    print ("1. Play number guessing game")
    print ("2. Exit")

    choice = input("Enter your choice from 1-2:")
    if choice == "1":
        number_guessing_game()
        continue
    elif choice == "2":
        print("Goodbye")
        break
    else:
        print ("Invalid Choice, Try again")