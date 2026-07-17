# AC 2.3 Git version control assessment :)

DATA_FILE = "users.txt"
def display_test_message():
    """Display a temporary message for testing."""
    print("Temporary feature is active.")

def request_user_name():
    """Ask the user to enter their name."""
    return input("Enter your name: ").strip()
def save_user_name(user_name):
    """Save the user's name to a text file."""
    with open(DATA_FILE, "a", encoding="utf-8") as user_file:
        user_file.write(user_name + "\n")
def display_main_menu():
    """Display the available menu options."""
    print("\nMain Menu")
    print("1. Display Welcome Message")
    print("2. Save Name")
    print("3. Exit")
def run_application():
    """Run the main app"""
    display_test_message()
    user_name = request_user_name()
    while True:
        display_main_menu()
        selected_option = input("Choose an option: ").strip()
        if selected_option == "1":
            print(f"Welcome, {user_name}!")
        elif selected_option == "2":
            save_user_name(user_name)
            print("Name saved successfully :)")
        elif selected_option == "3":
            print("Bye-bye! :)")
            break
        else:
            print("Please choose 1, 2 or 3.")
if __name__ == "__main__":
    run_application()