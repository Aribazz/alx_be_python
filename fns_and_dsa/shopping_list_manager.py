def display_menu():
    """
    Displays the menu options for the shopping list manager.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_to_add = input("Enter the item to add: ")  # Ensure this line matches exactly
            shopping_list.append(item_to_add)
            print(f"{item_to_add} has been added to the shopping list.")
        elif choice == '2':
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} has been removed from the shopping list.")
            else:
                print(f"{item_to_remove} is not in the shopping list.")
        elif choice == '3':
            print("Shopping List:")
            for item in shopping_list:
                print(f" {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
