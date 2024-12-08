import os
import sys
from modules.exception_module import MyException
from modules.read_json_module import read_json_content
from modules.empty_directory_module import empty_the_directory
from modules.create_structure_in_empty_folder_module import generate_structure_in_empty_folder

def create_structure(directory_path, json_path):
    if not os.path.isdir(directory_path):
        raise FileNotFoundError("Directory does not exist!")

    if not os.path.isfile(json_path):
        raise FileNotFoundError("JSON File does not exist!")

    if not json_path.endswith('.json'):
        raise MyException(f"File {os.path.basename(json_path)} is not JSON")
    
    empty_the_directory(directory_path)

    #generate_structure_in_empty_folder(directory_path, json_path)

if __name__ == "__main__":
    try:
        assert len(sys.argv) != 2, "There must be two parameters!"
    except Exception as e:
        print(e)

    create_structure(sys.argv[1], sys.argv[2])
