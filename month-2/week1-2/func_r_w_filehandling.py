# Read and Write to a File

# Script: read_write_file(input_path: str, output_path: str)
# Description: Create a script that reads from a file and writes the content to a new file with line numbers added.


def read_write_file(input_path, output_path):
    with open (input_path, "r") as i_file,  open(output_path, 'w') as o_file:
        for line in i_file:
            o_file.write(line)

input_path = 'msk_cluster_cmd'
output_path = 'output.txt'


read_write_file(input_path, output_path)

print(f"Content from {input_path} has been written to {output_path} with line numbers.")