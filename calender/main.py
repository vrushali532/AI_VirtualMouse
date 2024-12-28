
from menu_1 import menu_1
from menu_2 import menu_2

def main():
    while True:
        print("\nMenu:")
        print("1. Display specific month calendar")
        print("2. Display specific year calendar")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            menu_1.show_month_calendar()
        elif choice == "2":
            menu_2.show_year_calendar()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

