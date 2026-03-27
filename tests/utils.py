# utils.py

import os
import logging
from datetime import datetime

class Utils:
    @staticmethod
    def get_current_timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def create_directory(path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            return True
        except Exception as e:
            logging.error(f"Error creating directory: {str(e)}")
            return False

    @staticmethod
    def load_json(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Error loading JSON file: {str(e)}")
            return None

    @staticmethod
    def dump_json(data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            logging.error(f"Error dumping JSON data: {str(e)}")
            return False

import json