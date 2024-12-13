import os
import sys
from modules.read_json_module import read_json_content

def create_file_recursively(directory_path, dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            try:
                file_path = os.path.join(directory_path, key)
                os.mkdir(file_path)
            except Exception as e:
                print(e)

            create_file_recursively(file_path, value)

        elif isinstance(value, str):
            try:
                file_path = os.path.join(directory_path, key)
                f = open(f"{file_path}", "w")
                f.write(value)

            except Exception as e:
                print(e)

def generate_structure_in_empty_folder(directory_path, json_path):
    structure = read_json_content(json_path)
    
    create_file_recursively(directory_path, structure)
    
