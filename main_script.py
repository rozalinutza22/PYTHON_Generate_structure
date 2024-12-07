import os
import sys

class MyException(Exception):
    pass

def create_structure(directory_path, json_path):
    if not os.path.isdir(directory_path):
        raise FileNotFoundError("Directory does not exist!")

    if not os.path.isfile(json_path):
        raise FileNotFoundError("JSON File does not exist!")

    if not json_path.endswith('.json'):
        raise MyException(f"File {os.path.basename(json_path)} is not JSON")

if __name__ == "__main__":
    try:
        assert len(sys.argv) != 2, "There must be two parameters!"
    except Exception as e:
        print(e)

    create_structure(sys.argv[1], sys.argv[2])
