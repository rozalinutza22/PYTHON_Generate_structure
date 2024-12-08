import os
from exception_module import MyException

def empty_the_directory(directory_path):
    for root, directories, files in os.walk(directory_path):
        for fileName in files:
            file_path = os.path.join(directory_path, fileName)

            try:
                
                print(f"\nTrying to remove {fileName} ... ")
                os.remove(file_path)
                print(f"\nSuccessfully removed {fileName}")

            except PermissionError:
                raise MyException(f"\nInssuficient permissions to delete file {fileName}")
            except Exception as e:
                print(e)

