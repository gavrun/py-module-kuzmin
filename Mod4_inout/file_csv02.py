# Work with CSV file in Python (Dictionary)
import csv

filename = "data_02.csv"

# List of purchases
shoplist = {"apples": [12, 100], "pears": [31, 250], "carrots": [3, 35]}

#КлассCsvDictWriter(csvfile,Fieldnames,Restval='',Extrasaction='raise',Dialect='excel', *args, **kwds)
# Creates and returns the object for recording data as a dictionary of values ​​in the CSV file.

# Entry into a file
with open(filename, "w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
    writer.writeheader()                         # Writes headlines in a file
    for name, values in sorted(shoplist.items()):
        writer.writerow(dict(name=name, weight=values[0], price=values[1])) # Recalls the Row dictionary in CSV file


#ClassCsvDictReader(csvfile,Fieldnames=none,Restkey=none,Restval=none,Dialect='excel', *args, **kwds)
# Creates and returns an object for reading data from the CSV file as a dictionary of meanings.

# File reading
rows = []
with open(filename, "r", encoding="utf-8") as fh:
    reader = csv.DictReader(fh)
    rows = list(reader)  # Reader - an iterized object and can be converted into a list of lines

for row in rows:
    print(row)
