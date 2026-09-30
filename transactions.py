import csv
import os


def record_transaction(book_id, student_name, roll_no, action):
    file_exists = os.path.exists("transactions.csv")

    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Transaction ID",
                "Book ID",
                "Student Name",
                "Roll No.",
                "Action"
            ])

            transaction_id = "T1"

        else:
            with open("transactions.csv", "r", newline="") as read_file:
                row_count = sum(1 for _ in csv.reader(read_file)) - 1

            transaction_id = "T" + str(row_count + 1)

        writer.writerow([
            transaction_id,
            book_id,
            student_name,
            roll_no,
            action
        ])


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

    record_transaction(
        book_id,
        student_name,
        roll_no,
        "Issued"
    )

    print("Book issued successfully.")


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

    record_transaction(
        book_id,
        student_name,
        roll_no,
        "Returned"
    )

    print("Book returned successfully.")


def view_history():
    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)