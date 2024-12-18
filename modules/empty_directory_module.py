import os
import shutil
from modules.exception_module import MyException

def empty_the_directory(directory_path):
    
    for root, directories, files in os.walk(directory_path):
        for d in directories:
            try:
                print(f"\nTrying to remove {d}")
                dir_path = os.path.join(directory_path, d)
                shutil.rmtree(dir_path)
                print(f"\nSuccessfully removed {d}")
                
            except FileNotFoundError:
                raise MyException(f"Directory {d} does not exist!")
            except PermissionError:
                raise MyException(f"Insufficient permissions to delete {d}")
            except Exception as e:
                print(e)

        for file_name in files:
            file_path = os.path.join(directory_path, file_name)

            try:
                
                print(f"\nTrying to remove {file_name} ... ")
                os.remove(file_path)
                print(f"\nSuccessfully removed {file_name}")

            except PermissionError:
                raise MyException(f"\nInssuficient permissions to delete file {file_name}")
            except Exception as e:
                print(e)
            


