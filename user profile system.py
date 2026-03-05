# ==============================
# MASTERCLASS COMBINED PROJECT
# ==============================

import json
import os


# ==============================
# OOP SECTION
# ==============================

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_profile(self):
        print("\n===== USER PROFILE =====")
        print(f"Name  : {self.name}")
        print(f"Age   : {self.age}")
        print(f"Email : {self.email}")
        print("========================\n")


# ==============================
# FUNCTION SECTION
# ==============================

def save_user(user):
    """Save user data to JSON file"""
    data = {
        "name": user.name,
        "age": user.age,
        "email": user.email
    }

    with open("user_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("User data saved successfully!\n")


def load_user():
    """Load user data from JSON file"""
    if not os.path.exists("user_data.json"):
        print("No saved user found.\n")
        return None

    with open("user_data.json", "r") as file:
        data = json.load(file)

    return User(data["name"], data["age"], data["email"])


# ==============================
# MAIN PROGRAM (Loops + Exception Handling)
# ==============================

def main():
    while True:  # Loop for menu
        print("===== MASTER MENU =====")
        print("1. Create User Profile")
        print("2. View Saved Profile")
        print("3. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter Name: ")

                # Exception Handling for age
                try:
                    age = int(input("Enter Age: "))
                except ValueError:
                    print("Age must be a number!\n")
                    continue

                email = input("Enter Email: ")

                user = User(name, age, email)
                user.display_profile()
                save_user(user)

            elif choice == "2":
                user = load_user()
                if user:
                    user.display_profile()

            elif choice == "3":
                print("Exiting.. Thank you for making profile.")
                break

            else:
                print("Invalid choice. Try again.\n")

        except Exception as e:
            print("Unexpected Error:", e)


# Run program
if __name__ == "__main__":
    main()