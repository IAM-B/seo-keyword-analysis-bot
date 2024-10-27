import csv

# Define headers
headers = ["Keyword", "Monthly Average", "Total Search", "Quality Indice"]

# Read and sort rows based on "Quality Indice"
with open("final.csv", "r") as file:
    rows = csv.DictReader(file)
    sorted_rows = sorted(rows, key=lambda row: float(row["Quality Indice"]))

# Write sorted rows to a new file
with open("final_sorted.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(sorted_rows)
