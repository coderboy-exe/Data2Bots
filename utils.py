import os
import json

def resolve_dict(item: dict, output: dict, parent_key="")->dict:
    """
    Summary:
        Recursively resolves any JSON/dict passed to it into its component attributes

    Args:
        item (dict): The doctionary item to be parsed
        output (dict): the dictionary to be updated
        parent_key (str, optional): the parent dictionary contaiining that specific key. Defaults to "".

    Returns:
        dict: A formatted dictionary representation of the output
    """
    if not isinstance(item, dict):
        raise Exception("Invalid JSON argument")
    
    for key, val in item.items():
        value = ""
        current_key = f"{parent_key}.{key}" if parent_key else key
        
        if isinstance(val, str):
            value = "string"
        if isinstance(val, int):
            value = "integer"
        if isinstance(val, bool):
            value = "bool"
        if isinstance(val, list):
            if all(isinstance(item, dict) for item in val):
                value = "array"
                inner_dict_props = {}
                inner_dict = {
                    "type": value,
                    "tag": "",
                    "description": "",
                    "required": False,
                    "properties": inner_dict_props
                }
                for index, item in enumerate(val):
                    resolve_dict(item, inner_dict_props, f"{current_key}[{index}]")
                output[key] = inner_dict
                continue
            else:
                value = "enum"

        if isinstance(val, dict):
            value = "dict"
            inner_dict_props = {}
            inner_dict = {
                "type": value,
                "tag": "",
                "description": "",
                "required": False,
                "properties": inner_dict_props
            }
            resolve_dict(val, inner_dict_props, current_key)
            output[key] = inner_dict
            continue 
            
        output[key] = {
            "type": value,
            "tag": "",
            "description": "",
            "required": False
        }
    return output


def parse_from_file(filepath: str)->dict:
    """Reads a file's content and parses it accordingly

    Args:
        filepath (str): the path to the file

    Returns:
        dict: the parsed dictionary/JSON
    """
    if not os.path.exists(filepath):
        raise Exception("Source path does not exist")
    
    with open(file=filepath, mode="r", encoding="utf-8") as my_file:
        f = my_file.read()
        to_json = json.loads(f)
        message = to_json.get("message", {})
        output_data = resolve_dict(message, {})
                
        return output_data
    
    
def write_to_file(output_data: dict, folder: str, filename: str)->None:
    """_summary_

    Args:
        output_data (dict): _description_
        filepath (str): _description_
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    with open(file=f"{folder}/{filename}", mode="w", encoding="utf-8") as my_file:
            my_file.write(json.dumps(output_data, indent=3))


def get_all_json_files(path: str)->list:
    """Gets all json files in a folder

    Args:
        path (str): folder path

    Returns:
        list: a list of all the json files
    """
    if not os.path.exists(path):
        raise Exception("Source path does not exist")
    
    files = os.listdir(path)
    json_files = []
    for f in files:
        if f.endswith(".json"):
            json_files.append(f)
    
    return json_files