import csv
import os

def validate_csv(file_path):
    if not os.path.exists(file_path):
        print("File does not exist")
        return

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        row_count = 0
        
        for row in reader:
            row_count += 1
            if not row:
                print(f"Empty row at line {row_count}")

        print(f"Total rows checked: {row_count}")

if __name__ == "__main__":
    file_name = input("Enter CSV file path: ")
    validate_csv(file_name)
