import os
import json
import re


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def count_files_in_directory(root_path):
    directory_data = {}

    for folder_path, _, files in os.walk(root_path):
        folder_name = os.path.relpath(folder_path, root_path)
        folder_name = folder_name.replace(
            '\\', '/')  # Normalize directory names
        file_count = len(files)
        directory_data[folder_name] = file_count

    directory_data.pop('.', None)

    sorted_data = {key: directory_data[key] for key in sorted(
        directory_data, key=natural_sort_key)}
    json_data = json.dumps(sorted_data, indent=2)

    output_filename = os.path.join(root_path, "file_count_data.json")
    with open(output_filename, "w") as json_file:
        json_file.write(json_data)


root_directory_path = input("Enter the root directory path: ")

if os.path.exists(root_directory_path) and os.path.isdir(root_directory_path):
    count_files_in_directory(root_directory_path)
    print("JSON file created successfully in the root directory.")
else:
    print("Invalid directory path. Please provide a valid path.")
