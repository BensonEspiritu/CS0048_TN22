def display_menu():
    menu = {
        "Burger": 5,
        "Pizza": 10,
        "Salad": 7
    }
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")
    return menu

def calculate_bill(order, menu):
    total = 0
    print("\nOrder Summary:")
    
    for item, quantity in order.items():
        price = menu[item] * quantity
        total += price
        print(f"{item} x{quantity}: ${price}")
    
    service_charge = total * 0.10
    total_with_service = total + service_charge
    
    if total_with_service > 50:
        discount = total_with_service * 0.05
    else:
        discount = 0
        
    final_total = total_with_service - discount
    
    print(f"\nTotal: ${total}")
    print(f"Service Charge (10%): ${service_charge:.2f}")
    print(f"Discount (5% if > $50): -${discount:.2f}")
    print(f"Final Bill: ${final_total:.2f}")

def main():
    menu = display_menu()
    order = {}
    
    while True:
        item = input("Select an item (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        if item in menu:
            quantity_input = input(f"Enter quantity for {item}: ")
            if not quantity_input.isnumeric():
                print("Error: Please enter a valid quantity.")
                continue
            quantity = int(quantity_input)    
            if quantity <= 0:
                print("Error: Please enter a valid quantity.")
                continue
            
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Item not on the menu. Please choose again.")
    
    if not order:
        print("No orders were placed. Exiting.")
    else:
        calculate_bill(order, menu)

main()
