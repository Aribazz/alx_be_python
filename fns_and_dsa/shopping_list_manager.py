def display_menu():
    """Display the menu options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Core logic for managing the shopping list."""
    shopping_list = []  # Initialize an empty shopping list

    while True:
        # Display the menu
        display_menu()

        # Get user choice
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt the user to add an item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")

        elif choice == '2':
            # Prompt the user to remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid input
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
