while True:
    print ("\nMENU")
    print ("1. Add Scores")
    print ("2. Calculate Average")
    print ("3. Exit")

    choice = input("Enter your choice from 1-3:")

    if choice == "1":
        number_of_subjects = int(input("Enter number of subjects: "))
        entries = [(input("Enter subject name: "), int(input("Enter grade: "))) for _ in range(number_of_subjects)]
        scores = dict(entries)
        print(scores)
        
    elif choice == "2":
            average = sum(scores.values()) / len(scores)
            print(f"Average Grade: {average:.2f}")
        print(f"Average Grade: {average:.2f}")
    elif choice == "3": 
        print("Goodbye")
        break
    else:
        print ("Invalid Choice, Try again")