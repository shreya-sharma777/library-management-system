import csv

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