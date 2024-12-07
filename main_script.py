import os
import sys

def create_structure(directory_path, json_path):
    print("Hello")

if __name__ == "__main__":
    try:
        assert len(sys.argv) != 2, "There must be two parameters!"
    except Exception as e:
        print(e)

    create_structure(sys.argv[0], sys.argv[1])
