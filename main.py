#!/usr/bin/env python
import os
import sys

from utils import ( parse_from_file, 
                   write_to_file, 
                   resolve_dict, 
                   get_all_json_files 
                )

def main():
    """Entry point
    """
    if len(sys.argv) != 3:
        print(f"-----Please input a source and destination directory-----")
        print(f"Usage: ./main.py src_folder dest_folder\nUsage: python main.py src_folder dest_folder")
        return
    
    src = sys.argv[1]
    dest = sys.argv[2]

    files = get_all_json_files(src)
    for f in files:
        src_file = f"{src}/{f}"
        dest_filename = f"schema{f[-7:]}"
        
        data = parse_from_file(src_file)
        write_to_file(data, folder=dest, filename=dest_filename)




if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        
        