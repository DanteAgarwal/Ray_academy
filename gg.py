import os
import json
import re


def natural_sort_key(s):
    # Define a key function for natural sorting
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def count_files_in_directory(root_path):
    # Initialize an empty dictionary to store the file count data
    directory_data = {}

    # Walk through the directory recursively
    for folder_path, _, files in os.walk(root_path):
        folder_name = os.path.relpath(
            folder_path, root_path)  # Get the relative path
        file_count = len(files)

        # Add the file count to the directory data
        directory_data[folder_name] = file_count

    # Remove the root directory entry
    directory_data.pop('.', None)

    # Sort the keys in natural order
    sorted_data = {key: directory_data[key] for key in sorted(
        directory_data, key=natural_sort_key)}

    # Convert the sorted data to JSON format
    json_data = json.dumps(sorted_data, indent=2)

    # Save the JSON data to a file in the same directory as the root directory
    output_filename = os.path.join(
        root_path, "file_count_data.json")
    with open(output_filename, "w") as json_file:
        json_file.write(json_data)


# Specify the root directory path
root_directory_path = input("/path/to/your/root/directory")

# Call the function to create JSON data
count_files_in_directory(root_directory_path)

print("JSON file created successfully in the root directory.")
