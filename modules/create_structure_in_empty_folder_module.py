import os
import sys
from modules.exception_module import MyException
from modules.read_json_module import read_json_content

def generate_structure_in_empty_folder(directory_path, json_path):
    structure = read_json_content(json_path)
    print(type(structure))
