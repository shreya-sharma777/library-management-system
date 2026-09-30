import csv

def add_book():
    book_id = input("Enter book ID: ")

    book_exists = False

    with open("Book1.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == book_id:
                book_exists = True

    if book_exists:
        print("Book_Id already exists, please enter a different ID.")
        return

    book_name = input("Enter book name: ")
    author = input("Enter Author: ")
    category = input("Enter category: ")

    status = "Available"

    book = [book_id, book_name, author, category, status]

    with open("Book1.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(book)


def view_book():
    with open("Book1.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print(row[0], row[1], row[2], row[3], row[4])


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