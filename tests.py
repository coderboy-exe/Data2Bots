#!/usr/bin/env python
import unittest
import os
import json
from main import main

from utils import resolve_dict, parse_from_file, write_to_file, get_all_json_files
from constants import TEST_JSON_1, TEST_JSON_2, TEST_JSON_NO_MESSAGE_KEY, EXPECTED_SCHEMA_1, EXPECTED_SCHEMA_2

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.src_folder = "test_data/data"
        self.dest_folder = "test_data/schema"

        # Create temporary files and directories for testing
        write_to_file(TEST_JSON_1, self.src_folder, "test_data_1.json")
        write_to_file(TEST_JSON_2, self.src_folder, "test_data_2.json")
        write_to_file(TEST_JSON_NO_MESSAGE_KEY, self.src_folder, "test_data_no_msg.json")
        
    def test_get_all_json_files_exists(self):
        json_files = get_all_json_files(self.src_folder)
        self.assertEqual(len(json_files), 3)
   
    def test_get_all_json_files_not_exists(self):
        with self.assertRaises(Exception) as context:
            get_all_json_files("non_existent_folder")
            self.assertEqual(str(context.exception), "Source path does not exist")

    def test_parse_from_file(self):
        file_path = os.path.join(self.src_folder, "test_data_1.json")
        file_path2 = os.path.join(self.src_folder, "test_data_2.json")
        content = parse_from_file(file_path)
        content2 = parse_from_file(file_path2)
        write_to_file(content, self.dest_folder, "test_schema_1.json")
        write_to_file(content2, self.dest_folder, "test_schema_2.json")
        self.assertEqual(EXPECTED_SCHEMA_1, content)
        self.assertEqual(EXPECTED_SCHEMA_2, content2)
    
    def test_parse_from_file_not_exists(self):
        with self.assertRaises(Exception) as context:
            file_path = "fake_file"
            file_path2 = "another_fake"
            content = parse_from_file(file_path)
            content2 = parse_from_file(file_path2)
            self.assertEqual(str(context.exception), "Source path does not exist")
        
    def test_parse_from_file_no_message_key(self):
        file_path = os.path.join(self.src_folder, "test_data_no_msg.json")
        parsed = parse_from_file(file_path)
        self.assertEqual(dict, type(parsed))
        self.assertEqual(len(parsed), 0)
        self.assertEqual(parsed, {})
        
    def test_resolve_dict(self):
        resolved = resolve_dict(TEST_JSON_1, {})
        self.assertEqual(dict, type(resolved))
    
    def test_resolve_invalid_dict(self):
        with self.assertRaises(Exception) as context:
            invalid_json = ["test1", "test2"]
            resolved = resolve_dict(invalid_json, {})
            self.assertEqual(str(context.exception), "Invalid JSON argument")
    



if __name__ == '__main__':
    unittest.main()
