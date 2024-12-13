# Function to calculate and display the restaurant bill
def generate_bill():
    print("Welcome to the restaurant!")
    
    # Menu items and their prices
    menu = {
        "Burger": 100.00,
        "Pizza": 800.00,
        "Pasta": 170.00,
        "Salad": 50.00,
        "Soda": 120.00,
        "Water": 100.00
    }
    
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: Rs {price:.2f}")
    
    print("\nEnter the items you want to order. Type 'done' when finished.")
    
    # Initializing variables for the order and total price
    order = {}
    total_price = 0.0
    
    # Take user input for items ordered
    while True:
        item = input("\nEnter item name: ").capitalize()
        
        if item == "Done":
            break
        
        if item in menu:
            quantity = int(input(f"Enter quantity for {item}: "))
            order[item] = quantity
            total_price += menu[item] * quantity
        else:
            print("Sorry, that item is not on the menu.")
    
    # Display the order summary
    print("\nBill Summary:")
    for item, quantity in order.items():
        print(f"{item}: {quantity} x Rs {menu[item]:.2f} = Rs {menu[item] * quantity:.2f}")
    
    print(f"\nTotal Amount: Rs {total_price:.2f}")
    
    # Add tax (example: 10% tax)
    tax = total_price * 0.10
    total_with_tax = total_price + tax
    
    print(f"Tax (10%): Rs {tax:.2f}")
    print(f"Total Amount (with tax): pkr{total_with_tax:.2f}")
    print("\nThank you for dining with us!")

# Call the function to generate the bill
generate_bill()