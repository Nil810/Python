#Simple Shopping Cart Program where users can add, remove and view Items in their Cart using List.
# Shopping Cart Program using lists
def shopping_cart():
    cart = []

    while True:
        print("\nShopping Cart:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter item to add: ")
            cart.append(item)
            print(f"{item} added to cart.")

        elif choice == '2':
            if not cart:
                print("Cart is empty.")
            else:
                print("Cart:", cart)
                item_to_remove = input("Enter item to remove: ")
                if item_to_remove in cart:
                    cart.remove(item_to_remove)
                    print(f"{item_to_remove} removed from cart.")
                else:
                    print(f"{item_to_remove} not found in cart.")

        elif choice == '3':
            print("Shopping Cart:", cart)

        elif choice == '4':
            print("Checkout completed. Thank you!")
            break

        elif choice == '5':
            print("Exiting shopping cart program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Example usage:
shopping_cart()
