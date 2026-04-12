import csv

filename = input("Enter the CSV file name: ")

try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
        
    print("Total number of rows in the CSV file:", row_count)

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("An error occurred:", e)