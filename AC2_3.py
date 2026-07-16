def get_name():
    name = input("Enter your name: ")
    return name
def display_menu():
    print("\nMain Menu")
    print("1. Display Welcome Message")
    print("2. Exit")
user_name = get_name()
while True:
    display_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        print(f"Welcome, {user_name}!")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Please choose 1 or 2.")