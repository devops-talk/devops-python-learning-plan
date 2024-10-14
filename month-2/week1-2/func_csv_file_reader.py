# Function: read_csv(file_path: str)
# Description: Write a function that reads data from a CSV file and prints it in a formatted manner, handling any inconsistencies in the data.


import csv

def read_csv(csv_path):
    with open(csv_path, mode='r') as c_file:
        reader = csv.reader(c_file)
        headers = next(reader)  
        print(f"{' | '.join(headers)}")  

        for row in reader:
            formatted_row = [col if col != '' else 'N/A' for col in row] 
            print(f"{' | '.join(formatted_row)}")

read_csv('example.csv')
