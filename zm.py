from tabulate import tabulate

# Initialize lists to store inventory and orders
menu_items = []
customer_orders = []

# File paths for data storage
inventory_file = 'inventory.txt'
orders_file = 'orders.txt'

# Save inventory data to file
def save_inventory():
    with open(inventory_file, 'w') as file:
        headers = ["ID", "Name", "Price", "Availability"]
        data = [[item["id"], item["name"], item["price"], item["availability"]] for item in menu_items]
        table = tabulate(data, headers, tablefmt="grid")
        file.write(table)

# Save orders data to file
def save_orders():
    with open(orders_file, 'w') as file:
        headers = ["ID", "Name", "Item Name", "Quantity", "Status", "Price"]
        data = [[order["id"], order["name"], order["item_name"], order["quantity"], order["status"], order["price"]] for order in customer_orders]
        table = tabulate(data, headers, tablefmt="grid")
        file.write(table)

# Add an item to the inventory
def add_item(name, price, availability):
    id = len(menu_items) + 1
    item = {"id": id, "name": name, "price": price, "availability": availability}
    menu_items.append(item)
    print("Item added to the inventory.")
    save_inventory()

# Remove an item from the inventory
def remove_item(id):
    for item in menu_items:
        if item["id"] == id:
            menu_items.remove(item)
            print(f"Item with ID:{id} has been removed.")
            save_inventory()
            break
    else:
        print(f"Item with ID:{id} not found.")

# Update item availability in the inventory
def update_item_availability(id, availability):
    for item in menu_items:
        if item["id"] == id:
            item["availability"] = availability
            print(f"Item with ID:{id} has been updated.")
            save_inventory()
            break
    else:
        print(f"Item with ID:{id} not found.")

# Display the inventory
def display_inventory():
    if not menu_items:
        print("Inventory is empty.")
    else:
        headers = ["ID", "Name", "Price", "Availability"]
        data = [[item["id"], item["name"], item["price"], item["availability"]] for item in menu_items]
        print(tabulate(data, headers, tablefmt="grid"))

# Add a new customer order
def add_order(name, item_name, quantity, status, price):
    id = len(customer_orders) + 1
    order = {
        "id": id,
        "name": name,
        "item_name": item_name,
        "quantity": quantity,
        "status": status,
        "price": price
    }
    customer_orders.append(order)
    print("Your order has been successfully placed.")
    save_orders()

# Update the status of a customer order
def update_order_status(id, status):
    for order in customer_orders:
        if order["id"] == id:
            order["status"] = status
            print("Order status has been updated.")
            save_orders()
            break
    else:
        print("Order not found.")

# Review all customer orders
def review_orders():
    if not customer_orders:
        print("No orders yet.")
    else:
        headers = ["ID", "Name", "Item Name", "Quantity", "Status", "Price"]
        data = [[order["id"], order["name"], order["item_name"], order["quantity"], order["status"], order["price"]] for order in customer_orders]
        print(tabulate(data, headers, tablefmt="grid"))

# Main menu loop
while True:
    print("\nWelcome to Zomato Chronicles: The Great Food Fiasco")
    print("1. Add an item to the inventory")
    print("2. Remove an item from the inventory")
    print("3. Update item availability")
    print("4. Display item inventory")
    print("5. Add a new order")
    print("6. Update order status")
    print("7. Review all orders")
    print("8. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        availability = input("Is the item available? (yes/no): ")
        add_item(name, price, availability)
    elif choice == "2":
        id = int(input("Enter item ID to remove: "))
        remove_item(id)
    elif choice == "3":
        id = int(input("Enter item ID to update: "))
        availability = input("Update item availability (yes/no): ")
        update_item_availability(id, availability)
    elif choice == "4":
        display_inventory()
    elif choice == "5":
        name = input("Enter the customer's name: ")
        item_name = input("Enter the item you want to purchase: ")
        quantity = int(input("Enter the quantity: "))
        total_price = 0
        for item in menu_items:
            if item["name"] == item_name:
                total_price = item["price"] * quantity
                break
        status = input("Enter the status of the order (received/preparing/ready for pickup/delivered): ")
        add_order(name, item_name, quantity, status, total_price)
    elif choice == "6":
        id = int(input("Enter the order ID to update: "))
        status = input("Update the status (received/preparing/ready for pickup/delivered): ")
        update_order_status(id, status)
    elif choice == "7":
        review_orders()
    elif choice == "8":
        print("Thanks for using Zomato Chronicles.")
        save_inventory()
        save_orders()
        break
    else:
        print("Invalid choice. Please choose a valid option.")
