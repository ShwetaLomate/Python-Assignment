import json
import csv

# Input and output file names
json_file = input("Enter JSON file name: ")
csv_file = input("Enter CSV file name: ")

try:
    # Read JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)   # JSON array (list of dictionaries)

    # Check if data is not empty
    if len(data) == 0:
        print("JSON file is empty.")
    else:
        # Extract headers from keys of first dictionary
        headers = data[0].keys()

        # Write to CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print("JSON data successfully converted to CSV.")

except FileNotFoundError:
    print("Error: JSON file not found.")

except json.JSONDecodeError:
    print("Error: Invalid JSON format.")

except Exception as e:
    print("An error occurred:", e)