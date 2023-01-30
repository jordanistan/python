import csv


with open("phonebook.csv", "a") as file:
    name = input("Name: ")
    number = input("Number: ")
    email = input("Email: ")

    writer = csv.DictWriter(file, fieldnames=["name", "number", "email"])
    writer.writerow({"name": name, "number": number,"email": email})

file.close()