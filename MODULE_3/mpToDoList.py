task_counter = 1
to_do_list = {}
while True:
    print ("\nMENU")
    print ("1. Add Task")
    print ("2. View Task")
    print ("3. Remove Task")
    print ("3. Exit")

    choice = input("Enter your choice from 1-3: ")

    if choice == "1":
        task_name = input("Enter Task to add: ")
        to_do_list[task_counter] = task_name
        task_counter += 1
        continue
    elif choice == "2":
        print("\nTO DO LIST:")
        for key, value in to_do_list.items():
            print(f"{key}: {value}")
        continue
    elif choice == "3":
        task_to_remove = int(input("Enter the Task number to remove: "))
        if task_to_remove in to_do_list:
            to_do_list.pop(task_to_remove)
            print(f"Task {task_to_remove} has been removed")
        else:
            print("Task not found")
        continue
    elif choice == "4":    
        print("Goodbye!")
        break
    else:
        print ("Invalid Choice, Try again")