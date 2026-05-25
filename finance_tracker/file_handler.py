import json
import os


class FileHandler:
    @staticmethod
    def load_data(file_path):
        if not os.path.exists(file_path):
            return []

        with open(file_path, "r") as file:
            return json.load(file)

    @staticmethod
    def save_data(file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)