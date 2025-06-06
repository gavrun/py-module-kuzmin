# Work with CSV file in Python (sequence)
import csv

filename = "data_01.csv"

# List of purchases
shoplist = {"apples": [12, 100], "Pear": [31, 250], "carrot": [3, 35]}

# Entry into a file
with open(filename, "w", encoding="utf-8", newline="") as fh:
    writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
    writer.writerow(["Name", "weight", "price/kg."])  # The column headlines
    for name, values in sorted(shoplist.items()):
        writer.writerow([name, *values])
    writer.writerow(["rice", "4", "70"])  # Let us add arbitrary entry

# File reading
rows = []
with open(filename, "r", encoding="utf-8") as fh:
    reader = csv.reader(fh)
    rows = list(reader)   # Reader - an iterized object and can be converted into a list of lines

for row in rows:
    print(row)
