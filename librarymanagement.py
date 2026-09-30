#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
import csv

PROJECT_FOLDER = r"C:\Users\shreya sharma\OneDrive\Desktop\library management system"
os.chdir(PROJECT_FOLDER)

print(os.getcwd())
print(os.listdir())

import csv
def add_book():
    book_id=input("Enter book ID:")
    book_exists = False
    with open("Book1.csv","r")as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == book_id:
                book_exists = True
    if book_exists:
        print("Book_Id already exisits, please enter a different ID.")
        return
    book_name=input("Enter book name:")
    author=input("Enter Author:")
    category=input("Enter category:")
    status="Available"

    book = [book_id, book_name, author, category, status]

    with open("Book1.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(book)

add_book()

with open("Book1.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        print(row[0])


print(os.getcwd())



def view_book():
    with open("Book1.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row[0],row[1],row[2],row[3],row[4])



view_book()


def search_book():
    book_id=input("enter a Book_ID to search:")
    found = False
    with open("Book1.csv","r")as file:
        reader = csv.reader(file)
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == book_id:
                print(row)
                found=True
    if not found:
        print("book not found.")


search_book()


import os

def record_transaction(book_id, student_name, roll_no, action):
    file_exists = os.path.exists("transactions.csv")

    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Transaction ID", "Book ID", "Student Name", "Roll No.", "Action"])

        writer.writerow([
            "T" + str(len(open("transactions.csv").readlines())),
            book_id,
            student_name,
            roll_no,
            action
        ])


def record_transaction(book_id, student_name, roll_no, action):
    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        transactions = list(reader)

    transaction_id = "T" + str(len(transactions) + 1)

    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([transaction_id, book_id, student_name, roll_no, action])


def issue_book():
    book_id = input("Enter book ID to issue: ")
    rows = []
    book_found = False
    book_issued = False

    with open("Book1.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[0] == book_id:
                book_found = True

                if row[4] == "Available":
                    row[4] = "Issued"
                    book_issued = True
                else:
                    print("Book is already issued.")

            rows.append(row)

    if not book_found:
        print("Book not found.")
        return

    if not book_issued:
        return

    student_name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    with open("Book1.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    record_transaction(book_id, student_name, roll_no, "Issued")
    print("Book issued successfully.")


issue_book()


def return_book():
    book_id = input("Enter book ID to return: ")
    rows = []
    book_found = False
    book_returned = False

    with open("Book1.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[0] == book_id:
                book_found = True

                if row[4] == "Issued":
                    row[4] = "Available"
                    book_returned = True
                else:
                    print("Book is already available.")

            rows.append(row)

    if not book_found:
        print("Book not found.")
        return

    if not book_returned:
        return

    student_name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    with open("Book1.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    record_transaction(book_id, student_name, roll_no, "Returned")
    print("Book returned successfully.")


return_book()


def update_book():
    book_id = input("Enter book ID to update: ")
    rows = []
    book_found = False

    with open("Book1.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[0] == book_id:
                book_found = True

                print("Current Book Name:", row[1])
                print("Current Author:", row[2])
                print("Current Category:", row[3])

                row[1] = input("Enter new book name: ")
                row[2] = input("Enter new author: ")
                row[3] = input("Enter new category: ")

                print("Book updated successfully.")

            rows.append(row)

    if not book_found:
        print("Book not found.")
        return

    with open("Book1.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


def delete_book():
    book_id = input("Enter book ID to delete: ")
    rows = []
    book_found = False

    with open("Book1.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[0] == book_id:
                book_found = True
                print("Book deleted successfully.")
            else:
                rows.append(row)

    if not book_found:
        print("Book not found.")
        return

    with open("Book1.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


delete_book()


record_transaction("B001", "rahul", "101", "Returned")



def view_history():
    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)



view_history()



def library_report():
    total = 0
    available = 0
    issued = 0

    with open("Book1.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += 1

            if row[4] == "Available":
                available += 1
            elif row[4] == "Issued":
                issued += 1

    print("Total Books:", total)
    print("Available Books:", available)
    print("Issued Books:", issued)



library_report()



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

        else:
            print("Invalid choice. Please enter a number from 1 to 10.")



main_menu()


import csv

def search_book():
    book_id = input("Enter book ID to search: ")
    found = False

    with open("Book1.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == book_id:
                print(row)
                found = True

    if not found:
        print("Book not found.")


print("add_book:", "add_book" in globals())
print("view_book:", "view_book" in globals())
print("search_book:", "search_book" in globals())
print("record_transaction:", "record_transaction" in globals())
print("issue_book:", "issue_book" in globals())
print("return_book:", "return_book" in globals())
print("update_book:", "update_book" in globals())
print("delete_book:", "delete_book" in globals())
print("view_history:", "view_history" in globals())
print("library_report:", "library_report" in globals())

