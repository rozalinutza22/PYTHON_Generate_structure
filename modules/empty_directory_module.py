import os
import shutil
from modules.exception_module import MyException

def empty_the_directory(directory_path):
    # for root, directories, files in os.walk(directory_path):
    #     for fileName in files:
    #         file_path = os.path.join(directory_path, fileName)

    #         try:
                
    #             print(f"\nTrying to remove {fileName} ... ")
    #             os.remove(file_path)
    #             print(f"\nSuccessfully removed {fileName}")

    #         except PermissionError:
    #             raise MyException(f"\nInssuficient permissions to delete file {fileName}")
    #         except Exception as e:
    #             print(e)

    for root, directories, files in os.walk(directory_path):
        for d in directories:
            try:
                print(f"\nTrying to remove {d}")
                shutil.rmtree(directory_path)
            except FileNotFoundError:
                raise MyException(f"Directory {d} does not exist!")
            except PermissionError:
                raise MyException(f"Insufficient permissions to delete {d}")
            except Exception as e:
                print(e)


