# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == 'asc':
        sorted_list = sorted(products_list, key=lambda x: x[1])

    elif sort_order == 'desc':
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=True)

    else:
        print("Invalid sort order. Returning the original list.")
        return products_list

    return sorted_list


def display_products(products_list):
    print("Available Products:")
    for idx, (product, price) in enumerate(products_list, 1):
        print(f"{idx}. {product} - ${price}")

def display_categories():
    print("Available Product Categories:")
    for idx, category in enumerate(products.keys(), 1):
        print(f"{idx}. {category}")
    while True:
        try:
            category_choice = int(input("\nEnter the number of the category you'd like to explore: "))
            if 1 <= category_choice <= len(products):
                return category_choice - 1 
            else:
                print("Invalid choice!Please select a valid category number again:")
        except ValueError:
            print("Please enter a valid number!")
            



def add_to_cart(cart, product, quantity):
    product_name, price = product
    
    for item in cart:
        if item[0] == product_name:
            item_index = cart.index(item)
            current_quantity = item[2]
            cart[item_index] = (product_name, price, current_quantity + quantity)
            return
    
    cart.append((product_name, price, quantity))

def display_cart(cart):
    total_cost = 0  

    for product_name, price, quantity in cart:
        item_total = price * quantity 
        total_cost += item_total  
        print(f"{product_name} - ${price} x {quantity} = ${item_total}")  
    
    print(f"Total cost: ${total_cost:.2f}")  


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}") 
    print(f"Email: {email}")  
    print("Items Purchased:") 
    
    for product_name, price, quantity in cart:
        item_total = price * quantity  
        print(f"{quantity} x {product_name} - ${price} = ${item_total}")  
    
    print(f"Total: ${total_cost:.2f}")  
    print(f"Delivery Address: {address}")  
    print("Your items will be delivered in 3 days.")  
    print("Payment will be accepted upon delivery.")  

def validate_name(name):
    content = name.strip().split()

    if len(content) < 2:
        return False
    
    for part in content:
        if not part.isalpha():
            return False  
    return True  


def validate_email(email):
    email = email.strip()
    return "@" in email

def main():
    print("Welcome to an online shopping store!")
    
    #Enter and validate the name
    while True:
        name = input("Please enter your first name and last name ：")

        if validate_name(name):
            break
        else:
            print("Invalid name!")
            print("Please enter a valid name again(only alphabets): ")

    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email.")

    cart = []
    total_cost = 0

    while True:
        #user choose category
        category_index = display_categories()
        selected_category = list(products.keys())[category_index]
        print(f"Select one category: {selected_category}")

        #show all the products under selected category
        products_list = products[selected_category]
        while True:
            display_products(products_list)

            print("The options:")
            print("1. Select a product to buy")
            print("2. Sort the products according to the price")
            print("3. Go back to the category selection")
            print("4. Finish shopping")
            choice = input("Please enter your choice: ")
            
            if choice == '1':
                while True:
                    try:
                        #choose product
                        product_choice = int(input("Please enter the number of the product: ")) - 1
                        #validate product_choice
                        if 0 <= product_choice < len(products_list):
                            product = products_list[product_choice]
                            #choose quantity
                            while True:
                                quantity = input(f"Please enter the quantity for {product[0]}: ")
                                if quantity.isdigit() and int(quantity) > 0:
                                    quantity = int(quantity)
                                    #add product and update cost
                                    add_to_cart(cart, product, quantity)
                                    total_cost += product[1] * quantity
                                    print(f"Added {quantity} x {product[0]} to the cart.")
                                    break
                                else:
                                    print("Please enter a valid quantity again:")
                            break
                        else:
                            print("Please select a valid product number again:")
                    except ValueError:
                        print("Please enter a valid number again:")

            elif choice == '2':
                sort_number = input("Please enter a number to sort products (1 for ascending, 2 for descending): ")
                if sort_number in ['1', '2']:
                    if sort_number == '1':
                        sort_order = 'asc'
                    else:
                        sort_order = 'desc'

                    sorted_products = display_sorted_products(products_list, sort_order)
                    display_products(sorted_products)

                else:
                    print("Please select a number to sort again(1 or 2): ")
            
            elif choice == '3':
                break
                
            elif choice == '4':
                #finish shopping
                if cart:
                    print("Shopping Cart:")
                    display_cart(cart)
                    print(f"Total cost: ${total_cost}")
                    
                    address = input("Please enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
                return  

            else:
                print("Please enter the number(1,2,3,4) again:")

                

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
