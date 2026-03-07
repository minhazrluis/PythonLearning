import csv

# write messy data
with open("messy_students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade", "Email"])
    writer.writerow(["  alice  ", "20", "a", "ALICE@GMAIL.COM"])
    writer.writerow(["BOB  ", "abc", "B", "bob@gmail.com"])
    writer.writerow(["  Charlie", "21", "a-", "CHARLIE@YAHOO.COM"])
#read messy data and clean it
with open("messy_students.csv", "r") as f:
    reader = csv.DictReader(f)
    cleaned_data = []
    for row in reader:
        cleaned_row = {
            "Name": row["Name"].strip().title(),
            "Age": int(row["Age"]) if row["Age"].isdigit() else "Invalid Age",
            "Grade": row["Grade"].upper(),
            "Email": row["Email"].lower()
        }
        cleaned_data.append(cleaned_row)
#cleaned csv file
with open("cleaned_students.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age", "Grade", "Email"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in cleaned_data:
        writer.writerow(row)
#read cleaned data and print it
with open("cleaned_students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)