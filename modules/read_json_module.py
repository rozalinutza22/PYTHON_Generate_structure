import json
from exception_module import MyException

def read_json_content(json_path):
    try:

        with open(json_path) as f: 
            json_content= json.load(f)

    except json.JSONDecodeError as e:
        raise MyException(f"Error: Invalid JSON format. {e}")
    
    except UnicodeDecodeError:
        raise MyException("Error: Unable to decode the file. Please check the file's encoding.")
        
    except Exception as e:
        print(e)

    return json_content