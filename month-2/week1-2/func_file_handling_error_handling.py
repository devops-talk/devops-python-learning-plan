# Script: perform_operations()
# Description: Implement a script that performs multiple operations (e.g., file handling, data parsing) and logs any exceptions raised to an error log file.

import logging


logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def perform_operations():
    try:
        
        file_path = "data.txt"
        with open(file_path, 'r') as file:
            data = file.read()
            print(f"File data: {data}")

        
        str_numbers = ["10", "20", "abc", "30"]  
        parsed_numbers = []
        for num in str_numbers:
            try:
                parsed_numbers.append(int(num))
            except ValueError as e:
                logging.error(f"Failed to parse '{num}' to integer: {e}")
                print(f"Error: Failed to parse '{num}' to integer.")
        print(f"Parsed numbers: {parsed_numbers}")

        
        output_file = "output.txt"
        try:
            with open(output_file, 'w') as file:
                file.write("This is a test write operation.")
                print(f"Data successfully written to {output_file}")
        except Exception as e:
            logging.error(f"Error writing to file: {e}")
            print(f"Error writing to file: {e}")

    except FileNotFoundError as fnf_error:
        logging.error(f"File not found: {fnf_error}")
        print(f"Error: {fnf_error}")
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"Error: {e}")


perform_operations()
