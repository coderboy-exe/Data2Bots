#!/usr/bin/env python
import unittest
import os
import json
from main import main

from utils import resolve_dict, parse_from_file, write_to_file, get_all_json_files
from constants import TEST_JSON_1, TEST_JSON_2, EXPECTED_OUTPUT_1, EXPECTED_OUTPUT_2

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.src_folder = "test_data/data"
        self.dest_folder = "test_data/schema"

        # Create temporary files and directories for testing
        write_to_file(TEST_JSON_1, self.src_folder, "test_data_1.json")
        write_to_file(TEST_JSON_2, self.src_folder, "test_data_2.json")
        
    def test_get_all_json_files(self):
        test_files_path = os.path.join(self.src_folder)
        json_files = get_all_json_files(self.src_folder)
        self.assertEqual(len(json_files), 2)

    def test_parse_fromfile(self):
        file_path = os.path.join(self.src_folder, "test_data_1.json")
        file_path2 = os.path.join(self.src_folder, "test_data_2.json")
        content = parse_from_file(file_path)
        content2 = parse_from_file(file_path2)
        write_to_file(content, self.dest_folder, "test_schema_1.json")
        write_to_file(content2, self.dest_folder, "test_schema_2.json")
        self.assertEqual(TEST_JSON_1.get("message"), content)
        
    # def test_write_to_file(self):
    #     file_path_1 = os.path.join(self.src_folder, "test_schema_1.json")
    #     file_path_2 = os.path.join(self.src_folder, "test_schema_2.json")
    #     self.assertTrue(os.path.isfile(file_path_1))
    #     self.assertTrue(os.path.isfile(file_path_2))
   
        
    # def test_main(self):
    #     # Use the result of the write_to_file test to proceed with the main function
    #     test_file_path = os.path.join(self.src_folder, "test_file_1")
    #     dest_file_path = os.path.join(self.dest_folder, "test_file_schema")

    #     # Run main using the test file
    #     main(["", self.src_folder, self.dest_folder])

    #     # Assert that the destination file was created successfully
    #     self.assertTrue(os.path.isfile(dest_file_path))

    #     # Read the content from the destination file for further testing
    #     dest_content = read_from_file(dest_file_path)

    #     # Assert additional conditions based on the expected structure of the destination file
    #     # ...
    

    # def tearDown(self):
    #     # Clean up (delete) the temporary files
    #     for f in os.listdir(self.src_folder):
    #         file_path = os.path.join(self.src_folder, f)
    #         if os.path.isfile(file_path):
    #             os.remove(file_path)
    #     os.rmdir(self.src_folder)
        
    #     # if self.dest_folder:
    #     #     for f in os.listdir(self.dest_folder):
    #     #         file_path = os.path.join(self.dest_folder, f)
    #     #         if os.path.isfile(file_path):
    #     #             os.remove(file_path)
    #     # os.rmdir(self.dest_folder)
        
    #     os.rmdir("test_data")

if __name__ == '__main__':
    unittest.main()
