
# Log File Analysis

# Script: extract_errors(log_file: str, error_file: str)
# Description: Create a script that parses a log file, extracts error messages, and writes them to a separate file.

def extract_errors(log_file: str, error_file: str):
    error_keywords = ["ERROR", "FAIL", "EXCEPTION"] 
    
    with open(log_file, 'r') as log, open(error_file, 'w') as error_out:
        for line in log:
             if any(keyword in line for keyword in error_keywords):
                     error_out.write(line)

    print(f"Error messages have been extracted to {error_file}")

extract_errors('application.log', 'error_messages.log')
