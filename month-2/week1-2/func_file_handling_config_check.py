# Script: read_config(file_path: str)
# Description: Create a script that reads configuration values from a .ini or .yaml file and handles errors if the file is missing, malformed, or contains invalid keys.
import configparser
import yaml
import os

def read_config(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    _, ext = os.path.splitext(file_path)
    
    if ext == '.ini':
        config = configparser.ConfigParser()
        try:
            config.read(file_path)
            if not config.sections():
                raise ValueError(f"No valid sections found in '{file_path}'.")
            return dict(config)
        except configparser.Error as e:
            raise ValueError(f"Malformed INI file: {str(e)}")
    
    elif ext == '.yaml' or ext == '.yml':
        try:
            with open(file_path, 'r') as file:
                config = yaml.safe_load(file)
                if not isinstance(config, dict):
                    raise ValueError(f"Invalid content in YAML file '{file_path}'.")
                return config
        except yaml.YAMLError as e:
            raise ValueError(f"Malformed YAML file: {str(e)}")
    
    else:
        raise ValueError(f"Unsupported file type: '{ext}'")

# Example usage:
# config = read_config("config.ini") 
# config = read_config("config.yaml") 
