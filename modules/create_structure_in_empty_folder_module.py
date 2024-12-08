import os
import sys
from modules.read_json_module import read_json_content

def generate_structure_in_empty_folder(directory_path, json_path):
    structure = read_json_content(json_path)
    
    for key, value in structure.items():
        if isinstance(value, dict):
            print(f"{key} va fi folder")
        else:
            print(f"{key} va fi fisier")
    
