def get_name():
    name = input("Enter your name: ")
    return name
def save_name(name):
    with open("users.txt", "a") as file:
        file.write(name + "\n")
def display_menu():
    print("\nMain Menu")
    print("1. Display Welcome Message")
    print("2. Save Name")
    print("3. Exit")
user_name = get_name()
while True:
    display_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        print(f"Welcome, {user_name}!")
    elif choice == "2":
        save_name(user_name)
        print("Name now saved!")
    elif choice == "3":
        print("Bye Bye :) !")
        break
    else:
        print("Please choose 1, 2 or 3.")