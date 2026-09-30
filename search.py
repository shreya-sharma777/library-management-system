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