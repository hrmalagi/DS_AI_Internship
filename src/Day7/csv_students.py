import csv

with open("src/Day6/students.csv","r") as file:
    reader=csv.DictReader(file)
    print("Students who passed:")
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])