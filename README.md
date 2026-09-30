# Library Management System

# Library Management System

## 1. Project Overview

The Library Management System is a Python-based application developed to help a librarian manage basic library activities.

The system can store book details, search for books, issue and return books, update or delete records, maintain transaction history, and generate a simple library report.

## 2. Problem Statement

Managing library records manually can take time and may lead to mistakes. It can also be difficult to keep track of available and issued books.

This project provides a simple computerized system for managing book records and borrowing transactions using Python and CSV files.

## 3. Objectives

* To maintain book records digitally.
* To make searching for books easier.
* To manage issuing and returning of books.
* To maintain transaction history.
* To provide a quick library summary.
* To reduce errors in manual record keeping.

## 4. Features

1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Update Book
7. Delete Book
8. View Transaction History
9. Library Report
10. Exit

## 5. Project Structure

The project is divided into different Python files according to their functions.

* `main.py` - Contains the main menu and connects all modules.
* `books.py` - Handles adding, viewing, updating and deleting books.
* `search.py` - Handles book searching.
* `transactions.py` - Handles issuing, returning and transaction history.
* `reports.py` - Generates the library report.
* `validation.py` - Checks whether the menu choice is valid.
* `storage.py` - Stores the names of the CSV data files.

## 6. Technologies Used

* Python
* CSV files
* Visual Studio Code
* Jupyter Notebook

## 7. Data Storage

The project uses CSV files for storing data.

### Book1.csv

Stores:

* Book ID
* Book Name
* Author
* Category
* Status

### transactions.csv

Stores:

* Transaction ID
* Book ID
* Student Name
* Roll Number
* Action

## 8. Validation and Error Handling

The system handles common situations such as:

* Duplicate Book ID
* Book not found
* Issuing an already issued book
* Returning an already available book
* Invalid menu choice

## 9. How to Run

1. Open the project folder.
2. Make sure Python is installed.
3. Open the project folder in Visual Studio Code.
4. Make sure the required Python files and CSV files are present.
5. Open `main.py`.
6. Run `main.py` using the Python terminal.
7. Select an option from the main menu.

## 10. Testing

The main functions of the system were tested using a temporary test book with Book ID `TEST01`.

The following operations were tested:

* Adding a book
* Viewing books
* Searching for a book
* Issuing a book
* Returning a book
* Updating a book
* Deleting a book
* Viewing transaction history
* Generating a library report
* Invalid menu choice

## 11. Expected Users

The main user of this system is a librarian who needs to maintain book records and borrowing transactions.

## 12. Future Enhancements

The system can be improved in the future by adding:

* Login and authentication
* Due dates and fine calculation
* Student database
* Graphical user interface
* Database connectivity
* Automatic backup of records
