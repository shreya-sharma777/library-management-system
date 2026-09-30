from books import add_book, view_book, update_book, delete_book
from search import search_book
from transactions import issue_book, return_book, view_history
from reports import library_report
from validation import valid_menu_choice


def main_menu():

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Update Book")
        print("7. Delete Book")
        print("8. View Transaction History")
        print("9. Library Report")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if not valid_menu_choice(choice):
            print("Invalid choice. Please enter a number from 1 to 10.")
            continue

        if choice == "1":
            add_book()

        elif choice == "2":
            view_book()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            update_book()

        elif choice == "7":
            delete_book()

        elif choice == "8":
            view_history()

        elif choice == "9":
            library_report()

        elif choice == "10":
            print("Thank you for using the Library Management System!")
            break


if __name__ == "__main__":
    main_menu()