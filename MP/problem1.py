def calculate_calories(weight, duration, activity):
    if activity == 'walking':
        return 5 * duration * (weight / weight)  #calories burned for walking
    elif activity == 'running':
        return 10 * duration * (weight / weight)  #calories burned for running
    elif activity == 'cycling':
        return 8 * duration * (weight / weight)  #calories burned for cycling
    else:
        return None  #Invalid activity type

def main():
    weight_input = input("Enter your weight in kg: ")
    try:
        weight = float(weight_input)
        if weight < 0:
            print("Error: Weight cannot be negative.")
            return  #Exit the function
        
        total_calories_burned = 0
        
        while True:
            activity = input("Enter activity (walking/running/cycling) or 'exit' to finish: ").lower()
            if activity == 'exit':
                break
            
            duration_input = input(f"Enter duration of {activity} in minutes: ")
            try:
                duration = float(duration_input)
                if duration < 0:
                    print("Error: Duration cannot be negative.")
                    continue  
                
                calories_burned = calculate_calories(weight, duration, activity)
                if calories_burned is None:
                    print(f"Error: Invalid activity type: {activity}")
                    continue  
                
                total_calories_burned += calories_burned
                print(f"Calories burned for {activity}: {calories_burned:.2f} calories")

            except ValueError:
                print("Error: Invalid input. Please enter a valid number for duration.")
        
        print(f"Total calories burned: {total_calories_burned:.2f} calories")
        if total_calories_burned >= 500:
            print("Congratulations! You've burned a significant amount of calories.")

    except ValueError:
        print("Error: Invalid input. Please enter a valid number for weight.")


main()
